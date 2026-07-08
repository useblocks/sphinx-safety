# MIT License — Copyright (c) 2016-2025 useblocks GmbH
"""
Custom Sphinx-Needs dynamic functions for the safety classification docs.

``calculate_tcl`` computes the Tool Confidence Level (TCL) for a ``usecase``
need according to ISO 26262-8:2018 Annex B.
"""

# ISO 26262-8:2018 Annex B — Tool Confidence Level lookup table.
# Key: (TI, TD) → TCL  (all values as strings)
_TCL_TABLE: dict[tuple[str, str], str] = {
    ("1", "1"): "1",
    ("1", "2"): "1",
    ("1", "3"): "2",
    ("2", "1"): "1",
    ("2", "2"): "2",
    ("2", "3"): "3",
}


def calculate_tcl(app, need, needs, *args, **kwargs):
    """Return the Tool Confidence Level (TCL) for a ``usecase`` need.

    Reads ``ti`` from the use case and the ``td`` field from every linked
    ``feature`` (field ``features``). The worst-case TD (highest numeric
    value) across all features is used together with TI to look up the TCL
    according to ISO 26262-8:2018 Annex B.

    Returns ``"tbd"`` when TI is not set or when none of the linked features
    carry a numeric TD value yet.
    """
    if need is None:
        return "tbd"

    ti = (need.get("ti") or "").strip()
    if ti not in ("1", "2"):
        return "tbd"

    feature_ids = need.get("features") or []
    if not feature_ids:
        return "tbd"

    worst_td: int | None = None
    for fid in feature_ids:
        feature = needs.get(fid)
        if feature is None:
            continue
        # Features with no safety impact (si=no) do not need a TD value
        # and must not influence the TCL result.
        si = (feature.get("si") or "").strip()
        if si == "no":
            continue
        td_raw = (feature.get("td") or "").strip()
        if td_raw in ("1", "2", "3"):
            td_int = int(td_raw)
            if worst_td is None or td_int > worst_td:
                worst_td = td_int
        elif si == "yes":
            # Safety-relevant feature without a TD value → result incomplete.
            return "tbd"
        # si="" (undetermined) without td → skip conservatively

    if worst_td is None:
        return "tbd"

    return _TCL_TABLE.get((ti, str(worst_td)), "tbd")
