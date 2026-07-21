"""Rich content for the main service-category landing pages.

Each entry drives the full ``service_detail.html`` layout. Slugs match
``data/services.py``. Only categories with an entry here render the rich
layout; the rest fall back to the simple detail view. Image paths are
relative to ``static/`` (e.g. ``img/foo.jpg``); set to ``None`` for a
themed placeholder that is swapped later.
"""

# All appliance brand logos available in static/img/Brands.
_BRANDS = [
    ("Bosch", "bosch2.jpg"), ("Siemens", "siemens1.jpg"), ("Samsung", "samsung1.jpg"),
    ("LG", "lg2.jpg"), ("Whirlpool", "whirl-pool.jpg"), ("Ariston", "ariston.jpg"),
    ("Daewoo", "daewoo1.jpg"), ("Super General", "super-general.jpg"), ("Beko", "beko.jpg"),
    ("Midea", "midea.jpg"), ("Hitachi", "hitaachi.jpg"), ("Panasonic", "panasonic.jpg"),
    ("Electrolux", "electrolux1.jpg"), ("Teka", "teka.jpg"), ("AEG", "aeg.jpg"),
    ("Aftron", "aftron.jpg"), ("Carrier", "carrier1.jpg"), ("Eurotech", "eurotech.jpg"),
    ("Frigidaire", "figidaire.jpg"), ("Fujitsu", "fujitsu.jpg"), ("Goldstar", "goldstar.jpg"),
    ("Haier", "haier1.jpg"), ("Hisense", "hisence.jpg"), ("Ikon", "ikon.jpg"),
    ("Indesit", "indesit.jpg"), ("Maytag", "maytag.jpg"), ("Miele", "miele.jpg"),
    ("Philips", "philips.jpg"), ("Sanyo", "sanyo.jpg"), ("Simpson", "simpson.jpg"),
    ("Sony", "sony.jpg"), ("Toshiba", "toshiba-2.jpg"), ("Xiaomi", "xiaomi.jpg"),
    ("Zanussi", "zanussi.jpg"),
]

SERVICE_PAGES = {
    "home-appliances-repair": {
        "meta_title": "Home Appliance Repair in Dubai | Best Fix Technical Services",
        "meta_description": (
            "Same-day home appliance repair in Dubai — washing machines, "
            "fridges, ovens, dishwashers and small appliances. On-site "
            "diagnosis, clear pricing, warranty-backed work. Call +971 54 739 3716."
        ),
        "breadcrumb": "Home Appliances Repair",

        # ── 1. Hero ──
        "hero": {
            "h1_accent": "Same-Day",
            "h1": "Home Appliance Repair in Dubai",
            "sub": (
                "A leaking washing machine, warm refrigerator or faulty oven can "
                "bring the household routine to a stop. Best Fix provides "
                "professional home appliance repair in Dubai, with on-site "
                "diagnosis for washing machines, refrigerators, freezers, ovens, "
                "cookers, dishwashers and selected small appliances."
            ),
            "sub2": (
                "Same-day appointments are available for many repair requests. "
                "Emergency bookings are also accepted when a fault involves "
                "leaking water, sparking, burning smells or an appliance "
                "repeatedly tripping the electrical supply."
            ),
            "info": [
                "Call Best Fix: +971 54 739 3716",
                "Working hours: Saturday to Thursday, 8:00 am to 8:00 pm",
                "Emergency service: Available outside standard appointments",
            ],
            "image": "img/Professional Home appliances repair services.webp",
            "image_alt": "Best Fix technician repairing a home appliance in a Dubai home",
        },

        # ── 2. Diagnosis ──
        "diagnosis": {
            "h2": "Fast Appliance Repairs That Begin With the Right Diagnosis",
            "paras": [
                "Two appliances can show the same symptom for completely "
                "different reasons. A washing machine may stop draining because "
                "of a blocked filter, a damaged pump or a control fault. A "
                "refrigerator may feel warm because of poor airflow, a faulty "
                "sensor, a damaged fan or a compressor problem.",
                "Replacing parts without confirming the cause wastes time and money.",
                "A Best Fix technician inspects the appliance at your property, "
                "checks the relevant components and explains what has failed. You "
                "receive the repair recommendation and price before the approved "
                "work begins.",
            ],
            "list_title": "Our appliance repair service is available for:",
            "list": [
                "Apartments and villas",
                "Landlord-managed properties",
                "Holiday homes",
                "Offices and staff accommodation",
                "Property management companies",
                "Residential buildings and managed units",
            ],
        },

        # ── 3. Sub-services (alternating image / text) ──
        "services": {
            "h2": "Home Appliance Repair Services for Dubai Homes",
            "blocks": [
                {
                    "title": "Washing Machine Repair in Dubai",
                    "img": "washing machine repair.jpg",
                    "intro": (
                        "A faulty washing machine can leave clothes soaking wet, "
                        "trap water inside the drum or leak across the floor. Our "
                        "technicians inspect front-load, top-load, automatic and "
                        "semi-automatic washing machines."
                    ),
                    "list_title": "We attend washing machine faults such as:",
                    "faults": [
                        "Machine not switching on", "Drum not spinning",
                        "Water not draining", "Washer not filling",
                        "Door not opening or locking",
                        "Heavy shaking during the spin cycle",
                        "Loud banging, scraping or humming sounds",
                        "Water leaking from the door or hoses",
                        "Clothes remaining wet after the cycle",
                        "Error codes and control-panel faults",
                    ],
                    "note": (
                        "Stop using the machine if water is leaking near a socket "
                        "or electrical connection. Close the water valve and "
                        "disconnect the power only when it is safe."
                    ),
                },
                {
                    "title": "Fridge and Freezer Repair in Dubai",
                    "img": "fridge repair.jpg",
                    "intro": (
                        "Food can spoil quickly when a refrigerator stops cooling, "
                        "especially during Dubai's warmer months. A cooling problem "
                        "should be checked before the appliance is forced to run "
                        "continuously and the fault becomes more serious."
                    ),
                    "list_title": "Our refrigerator and freezer repair service covers:",
                    "faults": [
                        "Fridge not cooling", "Freezer not freezing",
                        "Excessive frost or ice", "Water collecting inside the unit",
                        "Refrigerator running without stopping",
                        "Unusual clicking or buzzing", "Damaged door seals",
                        "Faulty thermostat or temperature sensor",
                        "Internal fan problems", "Compressor and electrical faults",
                    ],
                    "note": (
                        "Do not keep changing the temperature control when the unit "
                        "is not cooling. Note any noise, display code or temperature "
                        "change and share those details when booking."
                    ),
                },
                {
                    "title": "Oven and Cooker Repair in Dubai",
                    "img": "cooking range, oven and stove repair.jpg",
                    "intro": (
                        "An oven that heats unevenly can burn food on one side "
                        "while leaving it undercooked on the other. Cooker ignition "
                        "faults and damaged controls can also create a safety "
                        "concern. Best Fix technicians inspect electric ovens, "
                        "cookers, built-in units, cooktops and selected gas appliances."
                    ),
                    "list_title": "Common oven and cooker faults include:",
                    "faults": [
                        "Oven not heating", "Weak or uneven heat",
                        "Temperature higher or lower than selected",
                        "Heating element failure", "Gas burner not igniting",
                        "Ignition clicking continuously", "Faulty thermostat",
                        "Damaged timer or control switch", "Cooker knob not responding",
                        "Door not closing correctly",
                        "Broken seal, hinge or internal light",
                    ],
                    "note": (
                        "Turn off the appliance immediately if you notice a gas "
                        "smell, visible spark or burning odour. Do not continue "
                        "testing it."
                    ),
                },
                {
                    "title": "Dishwasher Repair in Dubai",
                    "img": "dishwasher repair.jpg",
                    "intro": (
                        "A dishwasher should clean, rinse and drain without leaving "
                        "water or food residue behind. When one part of that cycle "
                        "fails, dishes may remain dirty or water may leak into the "
                        "kitchen."
                    ),
                    "list_title": "Our dishwasher repair service covers:",
                    "faults": [
                        "Dishwasher not starting", "Water not entering",
                        "Water not draining", "Plates remaining dirty",
                        "Cloudy or filmy glassware", "Appliance not heating",
                        "Dishes not drying", "Water leaking from the door",
                        "Blocked filter or spray arms", "Drain-pump faults",
                        "Error codes and control issues",
                    ],
                    "note": (
                        "Some drainage problems start with a blocked filter, but "
                        "persistent standing water usually needs a full inspection."
                    ),
                },
                {
                    "title": "Small Kitchen Appliance Repair",
                    "img": "small appliances repair.jpg",
                    "intro": (
                        "Best Fix also inspects selected small and built-in "
                        "household appliances. Service availability can depend on "
                        "the appliance type, model and availability of replacement "
                        "components."
                    ),
                    "list_title": "Contact us about repairs for:",
                    "faults": [
                        "Microwaves", "Electric cooktops and hobs",
                        "Cooker hoods and extractor fans", "Water heaters and geysers",
                        "Vacuum cleaners", "Irons", "Kettles", "Blenders", "Toasters",
                        "Other household electrical appliances",
                    ],
                    "note": (
                        "Send the brand, model number and a clear photograph when "
                        "booking. Our team will confirm whether the appliance can be "
                        "serviced."
                    ),
                },
            ],
        },

        # ── 4. Emergency ──
        "emergency": {
            "h2": "Emergency Appliance Repair in Dubai When the Fault Cannot Wait",
            "img": "emergency repair service.jpg",
            "para": (
                "Not every appliance problem is an emergency. A minor noise can "
                "often wait for a scheduled appointment. Active leaking, sparking "
                "and burning smells require faster attention."
            ),
            "list_title": "Request emergency appliance repair when:",
            "list": [
                "Water is spreading across the floor",
                "The appliance is sparking",
                "There is a burning or melting smell",
                "The circuit breaker trips whenever the appliance starts",
                "A refrigerator has completely stopped cooling",
                "A freezer is beginning to defrost",
                "An oven or cooker has an electrical or ignition fault",
                "The appliance will not switch off",
                "The fault may damage cabinets, flooring or nearby electrical fittings",
            ],
            "note": (
                "Switch off the appliance when it is safe. For a leaking washer or "
                "dishwasher, close the connected water valve. Do not repeatedly "
                "reset a breaker that trips again."
            ),
            "note2": (
                "Call +971 54 739 3716 and describe what is happening. Our team "
                "will confirm the earliest available appointment and provide "
                "immediate safety guidance where appropriate."
            ),
        },

        # ── 5. Same-day ──
        "sameday": {
            "h2": "Need Your Appliance Fixed Today?",
            "para": (
                "Same-day appliance repair appointments are available across many "
                "parts of Dubai, depending on the booking time, technician route, "
                "appliance model and parts required."
            ),
            "list_title": "To help us prepare, send:",
            "list": [
                "Your location", "Appliance type", "Brand and model number",
                "A short description of the fault",
                "Any error code shown on the display",
                "Photographs or a short video of the problem",
            ],
            "note": (
                "Providing these details before the visit can help the technician "
                "arrive with the tools and commonly required components for your "
                "appliance."
            ),
            "contact": "Call or WhatsApp: +971 54 739 3716",
        },

        # ── 6. Why choose (7 features) ──
        "why": {
            "h2": "Why Dubai Homeowners Choose Best Fix for Appliance Repair",
            "rows": [
                {"icon": "pin", "title": "On-Site Appliance Diagnosis",
                 "text": "The technician visits your apartment, villa or managed property. You do not need to transport a heavy washing machine, refrigerator or dishwasher to a workshop."},
                {"icon": "tag", "title": "Clear Pricing Before Repair",
                 "text": "The appliance is inspected before the repair cost is confirmed. The required work is explained so you can approve it before the technician proceeds."},
                {"icon": "users", "title": "Trained Technical Team",
                 "text": "Our technicians work with mechanical, electrical, drainage and electronic appliance faults. The repair is based on inspection rather than replacing parts by guesswork."},
                {"icon": "gear", "title": "Suitable Replacement Components",
                 "text": "When a component needs replacement, the technician selects a suitable part for the appliance model. Availability can vary by manufacturer and model age."},
                {"icon": "home", "title": "Careful Work Inside Your Property",
                 "text": "Repair work is carried out with attention to surrounding floors, cabinets and fittings. The work area is cleared after the repair."},
                {"icon": "check", "title": "Testing Before Completion",
                 "text": "Where site conditions allow, the appliance is tested after the repair. The technician checks the functions connected to the reported fault before completing the visit."},
                {"icon": "shield", "title": "Warranty-Backed Work",
                 "text": "Applicable repair and replacement work is supported by the relevant Best Fix warranty terms. Ask the team to confirm the coverage for your particular repair before work begins."},
            ],
        },

        # ── 7. How it works (6 steps) ──
        "steps": {
            "h2": "From First Call to Final Test: How Our Repair Service Works",
            "rows": [
                {"n": "01", "title": "Tell Us What Has Gone Wrong",
                 "text": "Call, WhatsApp or use the booking form. Share the appliance type, location, brand, model and symptoms."},
                {"n": "02", "title": "Choose an Available Appointment",
                 "text": "Our team confirms a suitable time. Same-day and emergency visits depend on technician availability and your location."},
                {"n": "03", "title": "Let the Technician Inspect the Appliance",
                 "text": "The technician checks the appliance and traces the fault to the affected component or system."},
                {"n": "04", "title": "Review the Repair Recommendation",
                 "text": "You receive an explanation of the fault and the proposed repair. No approved work begins before the price has been discussed."},
                {"n": "05", "title": "Repair and Replacement Work",
                 "text": "The technician completes the agreed repair using suitable tools and components."},
                {"n": "06", "title": "Functional Testing and Handover",
                 "text": "The repaired appliance is tested where possible. The technician explains the completed work and any care instructions before leaving."},
            ],
        },

        # ── 8. Brands (all 34 logos) ──
        "brands": {
            "h2": "Appliance Brands We Repair in Dubai",
            "intro": (
                "Best Fix technicians work on many appliance brands commonly "
                "installed in UAE homes. These include Bosch, Siemens, Samsung, "
                "LG, Whirlpool, Ariston, Daewoo, Super General, Beko, Midea, "
                "Hitachi, Panasonic, Electrolux and Teka."
            ),
            "note": (
                "We also inspect appliances from other manufacturers. Brand "
                "support does not mean every replacement part is immediately "
                "available. Send the full model number when booking so "
                "availability can be checked."
            ),
            "logos": [{"name": n, "img": "Brands/" + f} for n, f in _BRANDS],
        },

        # ── 9. Common problems ──
        "problems": {
            "h2": "Common Appliance Problems We Diagnose",
            "intro": "Contact Best Fix when an appliance:",
            "list": [
                "Will not switch on", "Stops halfway through a cycle",
                "Trips the circuit breaker", "Displays an error code",
                "Makes a new or unusually loud noise", "Leaks water",
                "Produces a burning smell", "Does not heat", "Does not cool",
                "Fails to drain", "Runs continuously", "Shakes or moves",
                "Leaves dishes or clothes unclean",
                "Has a damaged door, seal, switch or control panel",
            ],
            "note": (
                "A fault that appears small can place additional strain on other "
                "parts. Early inspection may prevent a blocked pump, damaged motor "
                "or electrical fault from becoming a larger repair."
            ),
        },

        # ── 10. Properties ──
        "properties": {
            "h2": "Appliance Repair for Apartments, Villas and Managed Properties",
            "paras": [
                "Appliance faults create different problems depending on the property.",
                "In an apartment, a leaking washing machine or dishwasher may "
                "damage the unit below. In a holiday home, a failed refrigerator "
                "can affect an arriving guest. In a managed property, delays can "
                "lead to repeated tenant complaints.",
            ],
            "list_title": "Best Fix accepts appliance repair bookings from:",
            "list": [
                "Homeowners", "Tenants", "Landlords", "Holiday-home operators",
                "Building managers", "Real estate companies",
                "Property maintenance coordinators",
            ],
            "note": (
                "For multiple appliances or several managed units, provide the "
                "property details and number of appliances when arranging the visit."
            ),
        },

        # ── 11. Areas ──
        "areas": {
            "h2": "Home Appliance Repair Across Dubai",
            "intro": (
                "Best Fix provides home appliance repair in JVC and communities "
                "throughout Dubai. Regular service locations include:"
            ),
            "list": [
                "Jumeirah Village Circle", "Dubai Marina", "Jumeirah Lake Towers",
                "JBR", "Downtown Dubai", "Business Bay", "Al Barsha", "Jumeirah",
                "Deira", "Bur Dubai", "Al Quoz", "Mirdif", "Dubai Silicon Oasis",
                "International City", "Dubai Sports City", "Discovery Gardens",
                "Al Furjan", "Arabian Ranches", "The Springs", "Palm Jumeirah",
                "Dubai South",
            ],
            "note": (
                "Appointments outside these areas may also be available. Send your "
                "building name or community when contacting the team."
            ),
        },

        # ── 12. Repair or replace ──
        "repair_replace": {
            "h2": "Repair or Replace the Appliance?",
            "paras": [
                "Repair is often practical when the appliance is otherwise in good "
                "condition and the fault involves a replaceable component. "
                "Replacement may be more sensible when the unit is heavily "
                "corroded, has repeated major faults or requires a costly "
                "component that is difficult to source.",
            ],
            "list_title": "Before deciding, consider:",
            "list": [
                "The age of the appliance", "Its overall physical condition",
                "Previous repairs", "Cost of the required work",
                "Availability of replacement parts", "Energy consumption",
                "Cost of a comparable new appliance",
                "Whether several major components are worn",
            ],
            "note": (
                "The technician can explain the immediate fault and required "
                "repair. The final decision remains yours."
            ),
        },

        # ── 13. Care tips ──
        "care": {
            "h2": "Simple Care That Helps Appliances Last Longer",
            "rows": [
                {"title": "Avoid Overloading the Washing Machine",
                 "text": "Heavy loads strain the motor, belt, bearings and suspension. Follow the stated drum capacity and spread large items evenly."},
                {"title": "Clean Accessible Filters",
                 "text": "Washing machines, dishwashers, refrigerators and cooker hoods may have filters that require regular cleaning. Follow the manufacturer's instructions."},
                {"title": "Keep Refrigerator Airflow Clear",
                 "text": "Do not pack food tightly against internal vents. Leave room around the appliance where required for heat to escape."},
                {"title": "Check Hoses and Connections",
                 "text": "Look for cracks, swelling, moisture and loose fittings around washing machine and dishwasher hoses."},
                {"title": "Use the Correct Detergent",
                 "text": "Too much detergent can create excessive foam, leave residue and affect drainage."},
                {"title": "Deal With New Noises Early",
                 "text": "Grinding, scraping and repeated clicking are not normal. Continued operation may damage another component."},
                {"title": "Keep Model Details Available",
                 "text": "A photograph of the rating label makes it easier to identify the correct appliance model when service or parts are required."},
            ],
        },

        # ── 14. FAQ ──
        "faq_h2": "Frequently Asked Questions",
        "faqs": [
            {"q": "How much does home appliance repair cost in Dubai?",
             "a": "The cost depends on the appliance, fault, model and required replacement components. The technician inspects the unit and explains the price before approved repair work begins."},
            {"q": "Is same-day appliance repair available?",
             "a": "Same-day appointments are available for many bookings. Availability depends on the time of your request, location, technician schedule and parts required."},
            {"q": "Do you provide emergency appliance repair?",
             "a": "Emergency service is available for urgent problems such as active leaks, sparking, burning smells, electrical tripping and complete refrigerator breakdowns. Call the team to confirm the earliest appointment."},
            {"q": "What appliances does Best Fix repair?",
             "a": "We repair washing machines, refrigerators, freezers, ovens, cookers, dishwashers and selected small household appliances."},
            {"q": "Can the technician repair the appliance at my home?",
             "a": "Many repairs can be completed at the customer's property. Some specialist faults or uncommon components may require additional work or another appointment."},
            {"q": "Do you repair all appliance brands?",
             "a": "Best Fix works with many common brands sold in the UAE. Service and parts availability depend on the specific model. Send the model number before booking."},
            {"q": "Should I continue using an appliance that is making noise?",
             "a": "A minor sound may have a simple cause, but grinding, scraping, banging or electrical buzzing should not be ignored. Stop using the appliance if the noise is accompanied by heat, smoke, leaking or a burning smell."},
            {"q": "What should I do when an appliance trips the breaker?",
             "a": "Switch the appliance off and unplug it when safe. Do not repeatedly reset the breaker. The fault may involve internal wiring, moisture, a heating component or another electrical part."},
            {"q": "Can you repair a leaking washing machine or dishwasher?",
             "a": "Yes. The technician can inspect hoses, seals, pumps, filters, valves and internal connections. Close the water supply if the leak is active."},
            {"q": "Is the repair covered by a warranty?",
             "a": "Applicable work is covered according to the warranty terms provided for the repair. Confirm the duration and coverage with the team before approving the work."},
            {"q": "What information should I provide when booking?",
             "a": "Send your location, appliance type, brand, model number, symptoms and any visible error code. Photographs or a short video can also be useful."},
            {"q": "What are your standard working hours?",
             "a": "Best Fix operates from Saturday to Thursday, 8:00 am to 8:00 pm. Friday is closed for standard appointments. Emergency service may be available outside normal booking hours."},
        ],

        # ── 15. Final CTA ──
        "cta": {
            "h2": "Book Same-Day Home Appliance Repair in Dubai",
            "sub": (
                "Do not let a leaking washer, warm refrigerator or faulty oven "
                "disrupt the rest of your day. Contact Best Fix and arrange an "
                "on-site appliance inspection at your Dubai property."
            ),
            "contact": [
                "Call or WhatsApp: +971 54 739 3716",
                "Email: info@bestfixit.ae",
                "Office: Prime Tower, 6th Floor, JVC, Dubai, UAE",
                "Standard hours: Saturday to Thursday, 8:00 am to 8:00 pm",
                "Friday: Closed for standard appointments",
                "Emergency service: Available",
            ],
        },
    },
}
