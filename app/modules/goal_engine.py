def suggest_goals(diagnosis, service):
    goals_map = {
        ("Dementia", "Personal Care"): [
            "Maintain independence in hygiene tasks",
            "Ensure safety at home",
            "Provide consistent routine and memory support"
        ],
        ("Stroke", "Nursing"): [
            "Support physical rehabilitation",
            "Prevent complications",
            "Ensure medication compliance"
        ]
    }
    return goals_map.get((diagnosis, service), ["Custom goals to be defined."])
