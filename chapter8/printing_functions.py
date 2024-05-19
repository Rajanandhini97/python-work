def print_models(unprinted_designs, completed_models):
    """Summarize the designs being printed"""
    print(f"\nFollowing designs are being printed: ")
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"-{current_design}")

        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Print completed model list"""
    print(f"\nFollowing are the completed models: ")
    for completed_model in completed_models:
        print(f"-{completed_model}")