"""
MkDocs-macros module: injects the training-environment values into pages.

Why this exists
---------------
Two environment profiles:
  - staging  -> staging.uipath.com. The participant environment: the newest
                Autopilot for Testers / Autopilot for Developers features are
                only available here. CI deploys with this profile.
  - prod     -> cloud.uipath.com. Kept for when those features reach
                Automation Cloud.

Pages reference the variables instead of hardcoding URLs/tenants, e.g.:

    !!! tip "Training Environment"
        Log in at **[{{ training_url }}]({{ training_url }})** using tenant **{{ training_tenant }}**.

Switch environments at build time with the COURSE_ENV variable:
    COURSE_ENV=staging mkdocs serve     # author/preview (and release: CI uses this)
    COURSE_ENV=prod    mkdocs build     # Automation Cloud variant

Default is "staging" so a plain build matches the release.
"""

import os

ENVIRONMENTS = {
    "staging": {
        "training_url": "https://staging.uipath.com/partnersuccess",
        "training_authority": "https://staging.uipath.com",
        "training_org": "partnersuccess",
        "training_tenant": "MadalinaTest",
        "training_folder": "AgenticTesting",
        "env_label": "UiPath staging",
    },
    "prod": {
        "training_url": "https://cloud.uipath.com/tpenlabs",
        "training_authority": "https://cloud.uipath.com",
        "training_org": "tpenlabs",
        "training_tenant": "AgenticTesting",
        "training_folder": "AgenticTesting",
        "env_label": "UiPath Automation Cloud",
    },
}


def define_env(env):
    profile = os.getenv("COURSE_ENV", "staging").lower()
    cfg = ENVIRONMENTS.get(profile, ENVIRONMENTS["staging"])
    for key, value in cfg.items():
        env.variables[key] = value
    env.variables["course_env"] = profile
