"""
MkDocs-macros module: injects the training-environment values into pages.

Why this exists
---------------
One environment profile:
  - prod     -> cloud.uipath.com/tpenlabs, tenant AgenticTestingWorkshop. The
                participant environment. CI deploys with this profile.

Pages reference the variables instead of hardcoding URLs/tenants, e.g.:

    !!! tip "Training Environment"
        Log in at **[{{ training_url }}]({{ training_url }})** using tenant **{{ training_tenant }}**.

Select the profile at build time with the COURSE_ENV variable:
    COURSE_ENV=prod mkdocs serve        # author/preview (and release: CI uses this)

Default is "prod" so a plain build matches the release. To add another
environment, add a profile to ENVIRONMENTS.
"""

import os

ENVIRONMENTS = {
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
