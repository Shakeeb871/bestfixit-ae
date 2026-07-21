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
    ("LG", "lg2.jpg"), ("Whirlpool", "whirl-pool.jpg"), ("Electrolux", "electrolux1.jpg"),
    ("AEG", "aeg.jpg"), ("Miele", "miele.jpg"), ("Beko", "beko.jpg"), ("Ariston", "ariston.jpg"),
    ("Indesit", "indesit.jpg"), ("Haier", "haier1.jpg"), ("Hisense", "hisence.jpg"),
    ("Midea", "midea.jpg"), ("Daewoo", "daewoo1.jpg"), ("Hitachi", "hitaachi.jpg"),
    ("Panasonic", "panasonic.jpg"), ("Toshiba", "toshiba-2.jpg"), ("Teka", "teka.jpg"),
    ("Zanussi", "zanussi.jpg"), ("Frigidaire", "figidaire.jpg"), ("Super General", "super-general.jpg"),
    ("Carrier", "carrier1.jpg"), ("Aftron", "aftron.jpg"), ("Eurotech", "eurotech.jpg"),
    ("Fujitsu", "fujitsu.jpg"), ("Goldstar", "goldstar.jpg"), ("Ikon", "ikon.jpg"),
    ("Maytag", "maytag.jpg"), ("Philips", "philips.jpg"), ("Sanyo", "sanyo.jpg"),
    ("Simpson", "simpson.jpg"), ("Sony", "sony.jpg"), ("Xiaomi", "xiaomi.jpg"),
]

SERVICE_PAGES = {
    "home-appliances-repair": {
        "meta_title": "Home Appliance Repair in Dubai | Best Fix Technical Services",
        "meta_description": (
            "Same-day home appliance repair in Dubai — washing machines, "
            "fridges, ovens, cookers and dishwashers. On-site diagnosis, clear "
            "pricing, warranty-backed work. Emergency support available."
        ),
        "breadcrumb": "Home Appliances Repair",

        # ── 1. Hero ──
        "hero": {
            "trustline": "Same-Day Appointments · Emergency Support · On-Site Diagnosis",
            "h1_accent": "Home Appliance Repair in Dubai",
            "h1": "When You Need It Most",
            "subheading": "One local team for washing machines, fridges, ovens, cookers and dishwashers.",
            "paras": [
                "An appliance breakdown rarely happens at a convenient time. The "
                "washing machine stops with water inside. The refrigerator begins "
                "losing temperature. The oven fails just before dinner, or the "
                "dishwasher starts leaking across the kitchen floor.",
                "Best Fix Technical Services provides professional home appliance "
                "repair in Dubai for apartments, villas, holiday homes and managed "
                "properties. Our technicians inspect the appliance at your "
                "location, identify the cause of the fault and explain the "
                "recommended repair before work begins.",
                "Same-day appointments are available for many service requests. "
                "Emergency support is also available for urgent problems involving "
                "leaking water, electrical tripping, sparks, burning smells or "
                "complete cooling failure.",
            ],
            "note": (
                "Appointment times depend on location, technician availability, "
                "appliance type and replacement-part requirements."
            ),
            "image": "img/Professional Home appliances repair services.webp",
            "image_alt": "Best Fix technician repairing a home appliance in a Dubai home",
        },

        # ── 2. Diagnosis ──
        "diagnosis": {
            "h2": "Appliance Repair Should Begin With Evidence, Not Guesswork",
            "paras": [
                "A fault code or visible symptom does not always reveal the "
                "complete problem.",
                "A washing machine that will not drain may have a blocked filter, "
                "damaged drain pump, obstructed hose or control-board fault. A "
                "refrigerator that feels warm may be affected by poor airflow, a "
                "worn door gasket, faulty thermostat, evaporator-fan problem or "
                "compressor issue.",
                "Replacing a component without checking the complete system can "
                "leave the original fault unresolved.",
                "Our technician examines the appliance, tests the systems "
                "connected to the reported problem and discusses the findings with "
                "you. The repair scope and expected price are explained before "
                "approved work begins.",
                "Best Fix has served homes and properties in Dubai since 2012, "
                "providing appliance repair alongside electrical, plumbing, HVAC "
                "and wider technical maintenance services.",
            ],
        },

        # ── 3. Sub-services ──
        "services": {
            "h2": "Home Appliance Repair Services Across Dubai",
            "blocks": [
                {
                    "title": "Washing Machine Repair That Gets the Cycle Moving Again",
                    "img": "washing machine repair.jpg",
                    "intro": (
                        "Modern washing machines depend on water valves, pressure "
                        "sensors, door locks, pumps, motors and electronic controls "
                        "working together. A problem in one part can prevent the "
                        "entire programme from completing."
                    ),
                    "types_title": "Best Fix technicians inspect:",
                    "types": [
                        "Front-load washing machines", "Top-load washing machines",
                        "Fully automatic machines", "Semi-automatic machines",
                        "Twin-tub washing machines", "Integrated washing machines",
                        "Washer-dryer combination units",
                    ],
                    "faults_title": "Common washing machine faults include:",
                    "faults": [
                        "Appliance not switching on", "Drum not turning",
                        "Machine not spinning", "Water not entering",
                        "Water remaining inside the drum", "Cycle stopping before completion",
                        "Clothes coming out soaking wet", "Door not locking",
                        "Door remaining locked", "Water leaking from the seal or hose",
                        "Machine shaking during the spin cycle",
                        "Grinding, banging or humming noises",
                        "Detergent remaining in the drawer",
                        "Error codes appearing on the display",
                        "Circuit breaker tripping during use",
                    ],
                    "components": (
                        "Depending on the symptoms, the technician may check the "
                        "inlet valve, drain filter, drain pump, pressure switch, "
                        "drive belt, motor, bearings, shock absorbers, door "
                        "interlock, wiring or electronic control board."
                    ),
                    "note": (
                        "Do not continue using a washing machine that is leaking "
                        "near an electrical connection. Close the water supply and "
                        "disconnect the appliance only when it is safe."
                    ),
                },
                {
                    "title": "Refrigerator and Freezer Repair Before Food Starts to Spoil",
                    "img": "fridge repair.jpg",
                    "intro": (
                        "Dubai's climate places a heavy demand on refrigeration "
                        "appliances. When a fridge or freezer loses temperature, "
                        "delaying an inspection can lead to spoiled food and place "
                        "additional strain on the cooling system."
                    ),
                    "types_title": "We inspect:",
                    "types": [
                        "Single-door refrigerators", "Double-door refrigerators",
                        "Top-freezer models", "Bottom-freezer models",
                        "Side-by-side refrigerators", "French-door refrigerators",
                        "Integrated refrigerators", "Upright freezers",
                        "Chest freezers", "Fridge-freezer combinations",
                    ],
                    "faults_title": "Book refrigerator or freezer repair when you notice:",
                    "faults": [
                        "Fridge not cooling", "Freezer not freezing",
                        "Temperature rising and falling", "Compressor running continuously",
                        "Heavy frost or ice buildup", "Water collecting inside the fridge",
                        "Water leaking underneath", "Unusual clicking or buzzing",
                        "Internal fan not running", "Food freezing inside the refrigerator section",
                        "Display panel showing an error", "Door not sealing correctly",
                        "Interior light or controls not working",
                    ],
                    "components": (
                        "The technician may inspect the thermostat, temperature "
                        "sensor, condenser coils, evaporator fan, condenser fan, "
                        "defrost heater, door gasket, relay, control board and "
                        "compressor circuit."
                    ),
                    "note": (
                        "Keep the doors closed as much as possible while waiting "
                        "for assistance. Avoid repeatedly changing the temperature "
                        "control, as this will not correct a mechanical or "
                        "electrical fault."
                    ),
                },
                {
                    "title": "Oven, Cooker and Hob Repair for Safer Everyday Cooking",
                    "img": "cooking range, oven and stove repair.jpg",
                    "intro": (
                        "An oven that does not reach the selected temperature can "
                        "leave food undercooked. A damaged cooker switch, faulty "
                        "heating element or ignition problem may also make the "
                        "appliance unsafe to operate."
                    ),
                    "types_title": "Best Fix provides inspection and repair support for:",
                    "types": [
                        "Freestanding ovens", "Built-in ovens", "Electric cookers",
                        "Gas cookers", "Ceramic hobs", "Electric hobs",
                        "Selected induction hobs", "Combination cooking appliances",
                    ],
                    "faults_title": "Common oven and cooker problems include:",
                    "faults": [
                        "Oven not heating", "Oven overheating",
                        "Temperature lower than selected", "Uneven cooking results",
                        "Heating element not working", "Grill function not operating",
                        "Burner not igniting", "Ignition clicking continuously",
                        "Cooker knob or switch not responding", "Timer or display not working",
                        "Oven door not closing properly", "Damaged hinge or door seal",
                        "Internal fan not running", "Appliance tripping the breaker",
                        "Burning smell during operation",
                    ],
                    "components": (
                        "The technician may examine heating elements, thermostats, "
                        "temperature probes, selector switches, ignition systems, "
                        "door seals, cooling fans, wiring and electronic controls."
                    ),
                    "note": (
                        "Stop using the appliance if you smell gas, see sparks or "
                        "notice melting, smoke or a strong electrical odour."
                    ),
                },
                {
                    "title": "Dishwasher Repair for Cleaner Dishes and a Drier Kitchen",
                    "img": "dishwasher repair.jpg",
                    "intro": (
                        "A dishwasher must fill, circulate, heat, rinse and drain "
                        "in the correct sequence. A fault at any stage can leave "
                        "dishes dirty, trap water inside the cabinet or cause a "
                        "leak around the kitchen."
                    ),
                    "types_title": "Our dishwasher repair service covers:",
                    "types": [
                        "Freestanding dishwashers", "Built-in dishwashers",
                        "Integrated dishwashers", "Compact dishwashers",
                    ],
                    "faults_title": "Contact us when your dishwasher:",
                    "faults": [
                        "Will not start", "Does not fill with water",
                        "Stops during the programme", "Leaves standing water inside",
                        "Does not drain", "Leaves food residue on dishes",
                        "Produces cloudy glassware", "Does not heat the water",
                        "Does not dry dishes", "Leaks from the door",
                        "Makes an unusual pump noise", "Has blocked or weak spray arms",
                        "Does not dispense detergent", "Shows an error code",
                        "Has a door that will not close",
                    ],
                    "components": (
                        "The inspection may include the inlet valve, circulation "
                        "pump, drain pump, filter, spray arms, heating element, "
                        "door latch, float switch, seals and control system."
                    ),
                    "note": (
                        "A filter can be cleaned by the user when the "
                        "manufacturer's instructions allow it. Recurring drainage, "
                        "heating or leakage problems should be checked by a "
                        "technician."
                    ),
                },
                {
                    "title": "Microwave and Small Appliance Repair",
                    "img": "small appliances repair.jpg",
                    "intro": (
                        "Some small household appliances can be repaired "
                        "economically, particularly built-in units or higher-value "
                        "models. Suitability depends on the appliance condition, "
                        "model and availability of compatible components."
                    ),
                    "types_title": "Contact Best Fix regarding selected:",
                    "types": [
                        "Microwave ovens", "Built-in microwaves", "Electric hobs",
                        "Cooker hoods", "Extractor fans", "Coffee machines",
                        "Vacuum cleaners", "Kettles", "Blenders", "Toasters",
                        "Irons", "Other domestic electrical appliances",
                    ],
                    "components": (
                        "Send the appliance brand, full model number and "
                        "photographs when requesting service. Our team will confirm "
                        "whether inspection and parts support are available."
                    ),
                    "note": (
                        "Microwave ovens contain high-voltage components that may "
                        "retain electrical charge after the appliance has been "
                        "unplugged. Internal microwave repairs should not be "
                        "attempted without suitable technical training."
                    ),
                },
            ],
        },

        # ── 4. Emergency ──
        "emergency": {
            "h2": "Emergency Appliance Repair in Dubai",
            "lead": "Some appliance faults should not wait.",
            "img": "emergency repair service.jpg",
            "para": (
                "A minor noise may be suitable for a scheduled appointment. Active "
                "leaking, electrical arcing and burning smells require faster "
                "attention."
            ),
            "list_title": "Request emergency appliance repair when:",
            "list": [
                "Water is spreading across the floor",
                "A washing machine or dishwasher is leaking continuously",
                "The appliance is sparking",
                "You notice smoke or a burning smell",
                "The plug, cable or socket is becoming hot",
                "The circuit breaker trips whenever the appliance starts",
                "A refrigerator has stopped cooling completely",
                "A freezer is beginning to defrost",
                "An oven or cooker will not switch off",
                "A door is jammed with water trapped inside",
                "The fault could damage flooring, cabinets or another property",
            ],
            "note": (
                "Switch off the appliance when it is safe to do so. For a leaking "
                "washing machine or dishwasher, close the connected water valve. "
                "Never touch a wet electrical socket, plug or extension cable."
            ),
            "explain_title": "When you call our team, explain:",
            "explain": [
                "Which appliance is affected",
                "What happened before the fault appeared",
                "Whether water, smoke or electricity is involved",
                "The appliance brand and model",
                "Any visible error code",
                "Your building and Dubai community",
            ],
            "note2": (
                "Our team will confirm the earliest available service window and "
                "provide practical safety guidance for the situation."
            ),
        },

        # ── 5. Same-day ──
        "sameday": {
            "h2": "Same-Day Appliance Repair Without Empty Promises",
            "lead": "A clear appointment window and an honest assessment.",
            "para": (
                "Many appliance repairs can be booked for the same day. The actual "
                "timing depends on the location, booking time, technician route, "
                "type of fault and whether the appliance needs a model-specific "
                "part."
            ),
            "list_title": "To help us prepare for the visit, send:",
            "list": [
                "Your Dubai location", "Appliance type", "Manufacturer",
                "Full model number", "Description of the problem",
                "Error code, when available", "Photograph of the rating label",
                "Short video showing the noise or fault",
            ],
            "note": (
                "This information helps the technician understand the reported "
                "problem before arriving. It does not replace an on-site diagnosis."
            ),
        },

        # ── 6. What we check first ──
        "checkfirst": {
            "h2": "What Our Appliance Technicians Usually Check First",
            "rows": [
                {"title": "When the washing machine will not drain",
                 "text": "The technician generally begins with the accessible filter and drain hose before testing the drain pump, pressure system and electrical supply to the pump."},
                {"title": "When the refrigerator is warm",
                 "text": "The door seal, airflow and temperature settings are checked before moving to the fans, sensors, defrost system, relay, control board and compressor circuit."},
                {"title": "When the oven is not heating",
                 "text": "The power supply and selected programme are confirmed first. Heating elements, thermostat, temperature sensor, selector switch and wiring are then checked as required."},
                {"title": "When the dishwasher leaves water inside",
                 "text": "The filter and drain path are inspected before testing the drain pump, float system, hose arrangement and electronic controls."},
                {"title": "When an appliance trips the breaker",
                 "text": "The appliance should remain disconnected until the technician checks for damaged wiring, moisture, insulation failure, a short circuit or a faulty motor or heating component."},
            ],
            "note": (
                "This step-by-step approach helps separate a simple blockage or "
                "connection issue from a component failure."
            ),
        },

        # ── 7. Brands ──
        "brands": {
            "h2": "Appliance Brands Commonly Found in UAE Homes",
            "intro": (
                "Best Fix works with many appliance manufacturers used in Dubai "
                "apartments and villas, subject to model knowledge and parts "
                "availability. Commonly requested brands include Bosch, Siemens, "
                "Samsung, LG, Whirlpool, Electrolux, AEG, Miele, Beko, Ariston, "
                "Indesit, Haier, Hisense, Midea, Daewoo, Hitachi, Panasonic, "
                "Toshiba, Teka, Zanussi, Frigidaire and Super General."
            ),
            "note": (
                "Models from the same manufacturer may use different pumps, "
                "sensors, motors, boards and control systems. Brand support does "
                "not mean that every replacement component is immediately "
                "available. Send a photograph of the rating label before the "
                "appointment whenever possible."
            ),
            "logos": [{"name": n, "img": "Brands/" + f} for n, f in _BRANDS],
        },

        # ── 8. Why choose ──
        "why": {
            "h2": "Why Dubai Homeowners Choose Best Fix",
            "intro": (
                "A Dubai maintenance company operating since 2012, Best Fix "
                "Technical Services supports homeowners, tenants, landlords and "
                "property managers with appliance repair and wider technical "
                "maintenance across Dubai."
            ),
            "rows": [
                {"icon": "pin", "title": "On-Site Appliance Diagnosis",
                 "text": "Our technicians visit apartments, villas, offices, holiday homes and managed properties. Most domestic appliances do not need to be transported before the initial inspection."},
                {"icon": "users", "title": "Licensed Technical Team",
                 "text": "Appliance faults may involve water, electricity, heating, cooling and moving mechanical components. Work is assigned to technicians with the relevant technical background."},
                {"icon": "tag", "title": "Clear Pricing Before Approved Work",
                 "text": "The fault and proposed repair are discussed before work begins. Any replacement requirement is explained so the customer can decide how to proceed."},
                {"icon": "gear", "title": "Model-Compatible Components",
                 "text": "When a component must be replaced, the part is selected according to the appliance model and technical specification, subject to availability."},
                {"icon": "check", "title": "Testing Before Handover",
                 "text": "Where conditions allow, the technician checks the functions related to the original fault, such as filling, draining, spinning, heating, cooling, sealing or control-panel operation."},
                {"icon": "home", "title": "Respect for the Property",
                 "text": "Technicians work around cabinets, flooring, water connections and electrical fittings with care. The immediate work area is cleared when the job is complete."},
                {"icon": "shield", "title": "Warranty-Backed Repair Work",
                 "text": "Eligible repairs and replacement work are covered according to the written warranty terms confirmed for the specific job."},
            ],
        },

        # ── 9. Steps ──
        "steps": {
            "h2": "From Booking to Final Test",
            "rows": [
                {"n": "01", "title": "Tell Us What Has Gone Wrong",
                 "text": "Call, WhatsApp or submit the service form. Share the appliance type, brand, model, location and symptoms."},
                {"n": "02", "title": "Receive a Service Window",
                 "text": "Our team checks the nearest available technician and confirms an appointment. Same-day and urgent visits are arranged where availability allows."},
                {"n": "03", "title": "On-Site Inspection",
                 "text": "The technician examines the appliance and tests the system connected to the fault."},
                {"n": "04", "title": "Fault Explanation",
                 "text": "You receive a practical explanation of the problem, proposed work and expected cost."},
                {"n": "05", "title": "Approved Repair",
                 "text": "The technician completes the agreed work using suitable tools and compatible components."},
                {"n": "06", "title": "Operational Check",
                 "text": "The appliance is tested where possible. The technician explains the completed repair and any relevant care advice."},
            ],
        },

        # ── 10. Properties ──
        "properties": {
            "h2": "Appliance Repair for Homes and Managed Properties",
            "list_title": "Our service is suitable for:",
            "list": [
                "Apartment residents", "Villa owners", "Tenants", "Landlords",
                "Holiday-home operators", "Property management companies",
                "Building supervisors", "Staff accommodation",
                "Offices with kitchens or laundry rooms",
                "Small commercial premises using domestic appliances",
            ],
            "notes": [
                "For a tenanted or managed property, provide the occupant's "
                "contact details, access instructions and repair-approval "
                "procedure when booking.",
                "For several faulty appliances, send separate model information and "
                "symptoms for each unit.",
            ],
        },

        # ── 11. Areas ──
        "areas": {
            "h2": "Home Appliance Repair Across Dubai",
            "intro": "Best Fix serves Jumeirah Village Circle and communities throughout Dubai, including:",
            "list": [
                "Jumeirah Village Circle", "Jumeirah Village Triangle", "Dubai Marina",
                "Jumeirah Lake Towers", "Jumeirah Beach Residence", "Downtown Dubai",
                "Business Bay", "Al Barsha", "Al Quoz", "Jumeirah", "Palm Jumeirah",
                "Dubai Hills Estate", "Arabian Ranches", "The Springs", "The Meadows",
                "Emirates Hills", "Dubai Sports City", "Motor City", "Discovery Gardens",
                "Al Furjan", "Dubai Silicon Oasis", "International City", "Mirdif",
                "Deira", "Bur Dubai", "Dubai South",
            ],
            "note": (
                "Coverage may also be available outside the listed communities. "
                "Share your building, community or nearest landmark when arranging "
                "an appointment."
            ),
        },

        # ── 12. Repair or replace ──
        "repair_replace": {
            "h2": "Repair or Replace the Appliance?",
            "para": (
                "A repair may be worthwhile when the appliance is otherwise in "
                "good condition and the fault involves a replaceable component."
            ),
            "list_title": "Replacement may be more practical when:",
            "list": [
                "The cabinet or chassis is heavily corroded",
                "Water has damaged several electrical sections",
                "The appliance has repeated major faults",
                "A critical component is no longer available",
                "Repair cost approaches the value of a replacement",
                "Several major parts are already worn",
                "The appliance consumes considerably more energy than a suitable newer model",
            ],
            "para2": (
                "Before deciding, consider the appliance's age, service history, "
                "physical condition, expected repair cost and availability of "
                "replacement parts."
            ),
            "note": (
                "The technician can explain the present fault and repair "
                "requirements. The final decision remains with the customer."
            ),
        },

        # ── 13. Care tips ──
        "care": {
            "h2": "Practical Appliance Care Between Service Visits",
            "rows": [
                {"title": "Do Not Overload Washing Machines",
                 "text": "An overloaded drum places additional pressure on the motor, belt, suspension and bearings. Follow the stated capacity and distribute bulky items evenly."},
                {"title": "Clean Accessible Filters",
                 "text": "Washing machines, dishwashers, refrigerators and cooker hoods may contain user-accessible filters. Clean them according to the manufacturer's instructions."},
                {"title": "Inspect Water Hoses",
                 "text": "Check washing machine and dishwasher hoses for cracks, swelling, loose fittings and moisture."},
                {"title": "Use the Correct Detergent",
                 "text": "Excess detergent can create too much foam, leave residue and interfere with drainage."},
                {"title": "Keep Refrigerator Airflow Clear",
                 "text": "Do not block internal vents with food containers. Maintain the ventilation space required around the appliance."},
                {"title": "Respond to Leaks Early",
                 "text": "A slow leak can damage flooring, kitchen units and the property below."},
                {"title": "Pay Attention to Unfamiliar Noises",
                 "text": "Grinding, scraping, knocking and repeated electrical clicking should not be treated as normal."},
                {"title": "Keep the Rating Label Readable",
                 "text": "The model and serial label may be needed to identify technical documentation or a compatible replacement part."},
            ],
        },

        # ── 14. FAQ ──
        "faq_h2": "Frequently Asked Questions",
        "faqs": [
            {"q": "How much does home appliance repair cost in Dubai?",
             "a": "The price depends on the appliance, model, fault and replacement components required. The technician inspects the appliance and explains the proposed repair cost before approved work begins."},
            {"q": "Can I book same-day appliance repair?",
             "a": "Same-day appointments are available for many requests. Availability depends on your location, booking time, technician route, fault type and parts requirements."},
            {"q": "Do you offer emergency appliance repair?",
             "a": "Emergency support is available for urgent problems such as active leaking, sparking, burning smells, electrical tripping and complete refrigerator or freezer cooling failure."},
            {"q": "Which home appliances do you repair?",
             "a": "Best Fix repairs washing machines, refrigerators, freezers, ovens, cookers, dishwashers and selected small household appliances."},
            {"q": "Can the appliance be repaired at my property?",
             "a": "Many faults can be diagnosed and repaired on site. A further visit may be required when a model-specific component must be obtained."},
            {"q": "Do you repair all appliance brands?",
             "a": "We work with many brands commonly used in the UAE. Service and component availability depend on the exact model, age and nature of the fault."},
            {"q": "What should I do when an appliance leaks?",
             "a": "Turn it off and close the connected water supply when safe. Keep water away from electrical fittings and do not use the appliance until it has been inspected."},
            {"q": "Why does my appliance trip the circuit breaker?",
             "a": "Possible causes include damaged wiring, moisture, insulation failure, a faulty heating element, motor trouble or an internal short circuit. Do not repeatedly reset the breaker while the appliance remains connected."},
            {"q": "Can an error code identify the broken part?",
             "a": "An error code identifies the system that detected a problem, but it does not always confirm the failed component. Testing is still required."},
            {"q": "Is the repair covered by a warranty?",
             "a": "Eligible work is covered according to the warranty terms provided for the job. The applicable duration and conditions should be confirmed before repair approval."},
            {"q": "What information should I send when booking?",
             "a": "Provide your address, appliance type, manufacturer, model number, symptoms and any displayed error code. A clear photograph or short video can also help."},
            {"q": "What are your working hours?",
             "a": "Regular appointments are available Saturday to Thursday from 8:00 am to 8:00 pm. Friday is closed for standard bookings. Emergency requests are handled separately, subject to availability."},
        ],

        # ── 15. Final CTA (the single place company details appear in full) ──
        "cta": {
            "h2": "Book Home Appliance Repair in Dubai",
            "sub": (
                "A faulty appliance does not need to disrupt the rest of your day. "
                "Contact Best Fix Technical Services for an on-site inspection and "
                "the earliest available appointment."
            ),
            "contact": [
                "Call or WhatsApp: +971 54 739 3716",
                "Email: info@bestfixit.ae",
                "Address: Prime Tower, 6th Floor, JVC, Dubai, UAE",
                "Regular hours: Saturday to Thursday, 8:00 am to 8:00 pm",
                "Friday: Closed for standard appointments",
                "Emergency support: Available subject to team availability",
            ],
        },
    },
}
