def select_workflow(features):
    N = features["num_assets"]

    if N <= 6:
        workflow = "QAOA"
    elif N <= 10:
        workflow = "HYBRID"
    else:
        workflow = "CLASSICAL"

    return workflow
