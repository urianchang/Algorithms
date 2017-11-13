import pprint

LIST_OF_OBJECTS = (
    {
        "name": "machine__source",
        "display_name": "Machine Name",
        "unit": "",
    },
    {
        "name": "machine__source_type",
        "display_name": "Machine Type",
        "unit": "",
    },
    {
        "name": "machine__factory_partner",
        "display_name": "Factory Partner",
        "unit": "",
    },
    {
        "name": "machine__factory_location",
        "display_name": "",
        "unit": "",
    },
    {
        "name": "machine__localtz",
        "display_name": "Machine Local Time Zone",
        "unit": "",
    },
    {
        "name": "machine__capturetime",
        "display_name": "",
        "unit": "",
    },
    {
        "name": "machine__capturetime_epoch",
        "display_name": "",
        "unit": "",
    },
    {
        "name": "machine__shift_ids",
        "display_name": "",
        "unit": "",
    },
    {
        "name": "machine__recipes",
        "display_name": "Machine Recipes",
        "unit": "",
    },
    {
        "name": "starttime",
        "display_name": "Start Time",
        "unit": "",
    },
    {
        "name": "starttime_epoch",
        "display_name": "Start Time (epoch)",
        "unit": "",
    },
    {
        "name": "endtime",
        "display_name": "End Time",
        "unit": "",
    },
    {
        "name": "endtime_epoch",
        "display_name": "End Time (epoch)",
        "unit": "ms",
    },
    {
        "name": "capturetime",
        "display_name": "Capture Time",
        "unit": "",
    },
    {
        "name": "capturetime_epoch",
        "display_name": "Capture Time (epoch)",
        "unit": "ms",
    },
    {
        "name": "total",
        "display_name": "Duration",
        "unit": "ms",
    },
    {
        "name": "shift",
        "display_name": "Shift",
        "unit": "",
    },
    {
        "name": "shiftid",
        "display_name": "Shift ID",
        "unit": "",
    },
    {
        "name": "metadata__downtime_type",
        "display_name": "Downtime Type",
        "unit": "",
    },
    {
        "name": "metadata__category",
        "display_name": "Downtime Category",
        "unit": "",
    },
    {
        "name": "metadata__category_code",
        "display_name": "",
        "unit": "",
    },
    {
        "name": "metadata__reason",
        "display_name": "Downtime Reason",
        "unit": "",
    },
    {
        "name": "metadata__reason_code",
        "display_name": "",
        "unit": "",
    },
    {
        "name": "reasoninfo__revision_history",
        "display_name": "",
        "unit": "",
    },
    {
        "name": "reasoninfo__latest_manual__reason_code",
        "display_name": "Manual - Reason Code",
        "unit": "",
    },
    {
        "name": "reasoninfo__latest_manual__author",
        "display_name": "Manual - Author",
        "unit": "",
    },
    {
        "name": "reasoninfo__latest_automated__reason_code",
        "display_name": "Automated - Reason Code",
        "unit": "",
    },
    {
        "name": "reasoninfo__latest_automated__author",
        "display_name": "Automated - Author",
        "unit": "",
    },
    {
        "name": "codes",
        "display_name": "",
        "unit": "",
    },
    {
        "name": "metadata__timezone",
        "display_name": "",
        "unit": "",
    },
    {
        "name": "localtz",
        "display_name": "Local Time Zone",
        "unit": "",
    },
    {
        "name": "status",
        "display_name": "Status",
        "unit": "",
    },
    {
        "name": "in_cycle",
        "display_name": "In Cycle",
        "unit": "",
    },
    {
        "name": "updatetime",
        "display_name": "Update Time",
        "unit": "",
    }
)

# THING = tuple(
#     field
#     for field_name in [
#         'machine__source', 'starttime', 'endtime', 'total', 'shift',
#         'metadata__downtime_type', 'metadata__category', 'metadata__reason'
#     ]
#     for field in LIST_OF_OBJECTS
#     if field['name'] == field_name
# )

THING = tuple(
    field
    for field in LIST_OF_OBJECTS
    if field['name'] in {'machine__source', 'starttime', 'endtime', 'total', 'shift',
    'metadata__downtime_type', 'metadata__category', 'metadata__reason'}
)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(THING)
