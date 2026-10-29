"""
MkDocs-macros module: injects the training-environment values into pages.

Why this exists
---------------
Two environment profiles:
  - prod     -> cloud.uipath.com/tpenlabs, tenant AgenticTestingWorkshop. The
                participant environment. CI deploys with this profile.
  - staging  -> staging.uipath.com/partnersuccess. Kept as a fallback.

Pages reference the variables instead of hardcoding URLs/tenants, e.g.:

    !!! tip "Training Environment"
        Log in at **[{{ training_url }}]({{ training_url }})** using tenant **{{ training_tenant }}**.

Switch environments at build time with the COURSE_ENV variable:
    COURSE_ENV=prod    mkdocs serve     # author/preview (and release: CI uses this)
    COURSE_ENV=staging mkdocs build     # staging variant

Default is "prod" so a plain build matches the release.
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
        "training_tenant": "AgenticTestingWorkshop",
        "training_folder": "AgenticTesting",
        "env_label": "UiPath Automation Cloud",
    },
}


def define_env(env):
    profile = os.getenv("COURSE_ENV", "prod").lower()
    cfg = ENVIRONMENTS.get(profile, ENVIRONMENTS["prod"])
    for key, value in cfg.items():
        env.variables[key] = value
    env.variables["course_env"] = profile
