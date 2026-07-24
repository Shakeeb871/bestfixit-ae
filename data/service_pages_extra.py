"""Rich content for the remaining core-service pages.

Same layout as ``home-appliances-repair`` (rendered by ``service_detail.html``)
but with content researched and written per trade. Image slots are left empty
on purpose — the template shows an "Image space" placeholder until real photos
are dropped in. Sections a page doesn't define are simply skipped.

``EXTRA_SERVICE_PAGES`` is merged into ``SERVICE_PAGES``.
"""

# Shared Dubai coverage list.
_AREAS = [
    "Downtown Dubai", "Dubai Marina", "Business Bay", "Jumeirah",
    "Palm Jumeirah", "Arabian Ranches", "Emirates Hills", "The Springs",
    "The Meadows", "Jumeirah Village Circle", "JLT", "Al Barsha",
    "Bur Dubai", "Deira", "Dubai Hills Estate", "Motor City",
    "Dubai Silicon Oasis", "International City", "Discovery Gardens",
    "Mirdif", "Al Quoz", "Dubai Sports City", "Al Furjan", "DIFC",
    "Dubai South", "JBR",
]


def _areas(trade):
    return {
        "h2": f"Areas We Cover for {trade} in Dubai",
        "intro": f"We provide {trade.lower()} across Dubai — apartments, villas, "
                 "offices, retail units and managed properties. Popular areas include:",
        "list": _AREAS,
        "note": "Don't see your area listed? We cover the whole of Dubai — just get "
                "in touch and we'll confirm a visit.",
    }


EXTRA_SERVICE_PAGES = {

    # ===================================================================== #
    # ELECTRICAL
    # ===================================================================== #
    "electrical-services": {
        "meta_title": "Electrical Services in Dubai | Licensed Electricians — Best Fix",
        "meta_description": (
            "Licensed electrical services in Dubai by Best Fix — wiring, DB boards, "
            "lighting, sockets, fault-finding and emergency repairs to DEWA standards. "
            "Same-day electricians, clear pricing, safe work."
        ),
        "breadcrumb": "Electrical Services",
        "hero": {
            "trustline": "Licensed Electricians · DEWA-Compliant · Emergency Support",
            "h1_accent": "Electrical Services in Dubai",
            "h1": "Done Safely, Done Right",
            "subheading": "Wiring, distribution boards, lighting, sockets and fault-finding for homes and businesses.",
            "paras": [
                "Electrical faults are rarely just an inconvenience — a tripping breaker, "
                "a warm socket or a flickering light can be the first sign of a wiring "
                "problem that shouldn't be ignored.",
                "Best Fix provides licensed electrical services across Dubai for apartments, "
                "villas, offices and managed properties. Every job is carried out to DEWA "
                "standards by qualified electricians who test, diagnose and explain the fault "
                "before any work begins.",
                "From a single socket to a full rewire or a new distribution board, we work "
                "cleanly, price clearly and leave the installation safe and certified.",
            ],
            "note": "Emergency support is available for tripping boards, burning smells, "
                    "sparks and total power loss.",
            "cta_label": "Book an Electrician",
        },
        "diagnosis": {
            "h2": "A Proper Diagnosis Before Any Electrical Work",
            "paras": [
                "Electrical work is only as safe as the diagnosis behind it. Our electricians "
                "start by testing the circuit, checking the load and inspecting connections, "
                "earthing and breaker ratings before touching anything.",
                "That means you get the actual cause of the fault — a loose connection, an "
                "overloaded circuit, ageing wiring or a failed component — not a guess, and a "
                "repair that's correct and compliant the first time.",
            ],
        },
        "services": {
            "h2": "Electrical Services We Provide",
            "blocks": [
                {"title": "Wiring & Rewiring",
                 "intro": "New wiring, partial rewires and full rewires for homes and offices, "
                          "installed to DEWA standards with the correct cable ratings and earthing.",
                 "types_title": "Where we help:", "types": ["New wiring points", "Partial rewires", "Full property rewires", "Concealed & surface wiring", "Cable upgrades"],
                 "note": "Ageing or overloaded wiring is a fire risk — we replace it safely and certify the work."},
                {"title": "Distribution Boards & Breakers",
                 "intro": "DB board installation, upgrades and repairs — nuisance tripping, "
                          "under-rated breakers, RCD/RCBO protection and safe load balancing.",
                 "types_title": "Common work:", "types": ["New DB boards", "Breaker replacement", "RCD / RCBO protection", "Load balancing", "Trip fault-finding"],
                 "note": "A board that trips repeatedly is protecting you from a fault — we find the cause, not just reset it."},
                {"title": "Lighting Installation",
                 "intro": "Indoor and outdoor lighting — downlights, chandeliers, LED upgrades, "
                          "dimmers, garden and facade lighting, wired and controlled cleanly.",
                 "types_title": "We install:", "types": ["Downlights & spotlights", "Chandeliers", "LED upgrades", "Dimmers & controls", "Outdoor & garden lighting"],
                 "note": "Switching to LED lowers your DEWA bill and the heat load on your home."},
                {"title": "Sockets, Switches & Fault-Finding",
                 "intro": "New and faulty sockets and switches, tingling or warm outlets, dead "
                          "circuits and intermittent faults traced back to the source.",
                 "types_title": "Typical calls:", "types": ["New sockets & switches", "Warm / discoloured outlets", "Dead circuits", "Intermittent faults", "USB & smart sockets"],
                 "note": "A warm socket or a mild tingle is urgent — switch the circuit off and call a licensed electrician."},
            ],
        },
        "emergency": {
            "h2": "Emergency Electrical Support",
            "lead": "Some electrical faults can't wait for a scheduled visit.",
            "para": "If your board keeps tripping, you can smell burning, you see sparks or "
                    "you've lost power completely, treat it as urgent. Switch off at the main "
                    "board where it's safe to do so and call us.",
            "list_title": "Call us straight away for:",
            "list": ["A distribution board that keeps tripping", "A burning smell from sockets, switches or the board", "Sparks or scorch marks", "A total or partial power loss", "A socket or appliance giving a mild shock"],
            "note": "Do not keep resetting a breaker that trips repeatedly — it is protecting the circuit from a real fault.",
            "explain_title": "What we do on an emergency call:",
            "explain": ["Make the installation safe first", "Isolate and identify the faulty circuit", "Explain the fault and the fix before proceeding"],
            "note2": "Once it's safe, we give you a clear picture of the repair and the cost before continuing.",
        },
        "checkfirst": {
            "h2": "Common Electrical Situations We Handle",
            "rows": [
                {"title": "When a Breaker Keeps Tripping", "text": "We test for overloaded circuits, a faulty appliance, moisture ingress or a failing breaker before deciding on the fix."},
                {"title": "When Lights Flicker or Dim", "text": "Flickering often points to a loose connection or an overloaded circuit — we trace it back rather than mask it."},
                {"title": "When a Socket Feels Warm", "text": "A warm or discoloured socket usually means a loose connection or overload. We isolate it and repair it safely."},
                {"title": "When You're Renovating", "text": "New wiring, extra points, lighting and a suitable board are planned around your layout and future load."},
            ],
            "note": "Every visit ends with the circuit tested and left safe — no live wire left guessed at.",
        },
        "why": {
            "h2": "Why Choose Best Fix for Electrical Work",
            "intro": "Electrical work is not the place to cut corners. Here's why Dubai homeowners and businesses call us.",
            "rows": [
                {"icon": "shield", "title": "Licensed & Compliant", "text": "Work carried out to DEWA standards by qualified electricians — correct ratings, wiring and earthing."},
                {"icon": "check", "title": "Proper Fault-Finding", "text": "We diagnose the real cause with testing, not guesswork, so the fix holds."},
                {"icon": "gear", "title": "Clean, Certified Work", "text": "Tidy installation, safe connections and a clear account of what was done."},
                {"icon": "users", "title": "Homes & Businesses", "text": "Apartments, villas, offices, retail and managed properties across Dubai."},
                {"icon": "pin", "title": "Same-Day & Emergency", "text": "Fast response for urgent faults, with same-day slots wherever possible."},
                {"icon": "tag", "title": "Clear Pricing", "text": "You know the cost before we start — no surprises on the invoice."},
            ],
        },
        "steps": {
            "h2": "How It Works",
            "rows": [
                {"n": "1", "title": "Book a Visit", "text": "Call or message us with the fault or the job and we'll arrange a slot."},
                {"n": "2", "title": "On-Site Testing", "text": "The electrician tests and inspects to find the real cause."},
                {"n": "3", "title": "Clear Quote", "text": "You get the fault explained and a clear price before work starts."},
                {"n": "4", "title": "Safe Repair", "text": "We carry out the work to standard and test the circuit."},
                {"n": "5", "title": "Left Certified", "text": "The installation is left safe, tidy and working as it should."},
            ],
        },
        "areas": _areas("Electrical Services"),
        "care": {
            "h2": "Simple Electrical Safety Tips",
            "rows": [
                {"title": "Don't Overload Sockets", "text": "Avoid daisy-chaining extension leads on one outlet, especially with high-load appliances."},
                {"title": "Act on Warm Sockets", "text": "A warm, buzzing or discoloured socket needs checking — switch it off and call an electrician."},
                {"title": "Test Your RCD", "text": "If your board has a test button, press it occasionally to confirm the safety trip works."},
                {"title": "Mind Water & Power", "text": "Keep sockets and appliances away from water, and never handle them with wet hands."},
                {"title": "Use the Right Bulbs", "text": "Stay within the fitting's rated wattage and switch to LED to cut heat and cost."},
                {"title": "Never Ignore a Burning Smell", "text": "A burning smell or scorch mark means stop using the circuit and get it inspected immediately."},
            ],
        },
        "faq_h2": "Electrical Services FAQs",
        "faqs": [
            {"q": "Why does my breaker keep tripping?", "a": "A breaker that trips repeatedly is usually reacting to an overloaded circuit, a faulty appliance, moisture or a wiring fault. We test the circuit to find the exact cause rather than simply resetting it."},
            {"q": "Are your electricians licensed?", "a": "Yes. Our electrical work is carried out to DEWA standards by qualified electricians, with correct breaker ratings, wiring and earthing."},
            {"q": "Can you help in an emergency?", "a": "Yes. For tripping boards, burning smells, sparks or total power loss we prioritise the call, make the installation safe first, then diagnose and repair."},
            {"q": "Do you handle both homes and offices?", "a": "We work across apartments, villas, offices, retail units and managed properties throughout Dubai."},
            {"q": "Can you upgrade my lighting to LED?", "a": "Yes. LED upgrades lower your DEWA bill and reduce heat. We handle downlights, chandeliers, dimmers and outdoor lighting."},
            {"q": "Will you give me a price before starting?", "a": "Always. After testing we explain the fault and give you a clear price before any work begins."},
        ],
    },

    # ===================================================================== #
    # HVAC
    # ===================================================================== #
    "hvac-services": {
        "meta_title": "AC & HVAC Services in Dubai | Repair, Service & Install — Best Fix",
        "meta_description": (
            "AC and HVAC services in Dubai by Best Fix — air-conditioning repair, "
            "servicing, gas top-up, duct cleaning and new installation for split, "
            "ducted and central systems. Same-day cooling repairs."
        ),
        "breadcrumb": "HVAC Services",
        "hero": {
            "trustline": "Same-Day Cooling Repairs · Servicing · Installation",
            "h1_accent": "AC & HVAC Services in Dubai",
            "h1": "Cool, Clean and Efficient",
            "subheading": "Repair, servicing, gas top-up, duct cleaning and installation for split, ducted and central systems.",
            "paras": [
                "In Dubai an air conditioner isn't a luxury — it runs most of the year and "
                "works far harder than in most climates. When cooling drops or a unit fails, "
                "it needs sorting quickly.",
                "Best Fix provides complete AC and HVAC services across Dubai for apartments, "
                "villas, offices and managed properties. We repair, service and install split, "
                "ducted and central systems, always starting with a proper inspection.",
                "Regular servicing keeps cooling strong, lowers your DEWA bill and catches "
                "small faults before they become a breakdown on the hottest day of the year.",
            ],
            "note": "Same-day appointments are available for weak cooling, water leaks and complete cooling failure.",
            "cta_label": "Book AC Service",
        },
        "diagnosis": {
            "h2": "We Diagnose the Cause, Not Just the Symptom",
            "paras": [
                "Weak cooling can be low gas, a dirty coil, a failing compressor, a blocked "
                "drain or a thermostat fault — and topping up gas on a system that's leaking "
                "only hides the problem. Our technicians inspect the whole system first.",
                "You get an honest diagnosis and a repair that lasts, whether that's a clean "
                "and service, a genuine part, tracing a gas leak or advising when a tired unit "
                "is better replaced.",
            ],
        },
        "services": {
            "h2": "HVAC Services We Provide",
            "blocks": [
                {"title": "AC Repair & Fault-Finding",
                 "intro": "Weak or warm airflow, water leaks, strange noises, tripping units and "
                          "systems that won't switch on — diagnosed and repaired.",
                 "types_title": "We work on:", "types": ["Split & wall-mounted units", "Ducted / concealed systems", "Central AC", "Cassette units", "Window units"],
                 "note": "A sudden jump in your DEWA bill often means the system is straining — worth a check."},
                {"title": "AC Servicing & Maintenance",
                 "intro": "Full servicing — coil and filter cleaning, gas check, drain clearing "
                          "and performance testing — to keep cooling strong and efficient.",
                 "types_title": "A service covers:", "types": ["Filter & coil cleaning", "Gas pressure check", "Drain line clearing", "Electrical & thermostat check", "Performance test"],
                 "note": "In Dubai's climate we recommend a service every few months, not once a year."},
                {"title": "Gas Top-Up & Leak Repair",
                 "intro": "Refrigerant top-ups done properly — with the leak traced and repaired "
                          "first, so cooling is restored and stays restored.",
                 "types_title": "Included:", "types": ["Leak detection", "Leak repair", "Refrigerant top-up", "Pressure testing", "Cooling verification"],
                 "note": "Topping up gas without fixing the leak is a short-term patch — we do it right."},
                {"title": "Duct Cleaning & Installation",
                 "intro": "Duct cleaning for cleaner, healthier air, and full installation of new "
                          "split, ducted and central systems sized to the space.",
                 "types_title": "We handle:", "types": ["Duct cleaning", "New split installation", "Ducted system install", "Unit relocation", "Thermostat upgrades"],
                 "note": "Clean ducts and a correctly sized system mean better air and lower running costs."},
            ],
        },
        "emergency": {
            "h2": "Same-Day AC Support",
            "lead": "In the Dubai heat, a failed AC is an emergency.",
            "para": "When a unit stops cooling completely, leaks water across the floor or trips "
                    "the power, we prioritise the call and aim to get to you the same day.",
            "list_title": "We respond quickly to:",
            "list": ["A unit that has stopped cooling entirely", "Water leaking from the indoor unit", "An AC that trips the breaker", "Loud grinding or rattling", "A burning or musty smell when it runs"],
            "note": "Turn the unit off if it's leaking or tripping, and keep the room closed to hold the cool while you wait.",
            "explain_title": "On the visit we:",
            "explain": ["Inspect the full system", "Identify the real cause", "Explain the fix and cost before starting"],
            "note2": "You get a clear diagnosis and price before we carry out any repair.",
        },
        "checkfirst": {
            "h2": "Common AC Situations We Handle",
            "rows": [
                {"title": "When Cooling Feels Weak", "text": "We check gas pressure, the coils, filters and the compressor rather than assuming it just needs gas."},
                {"title": "When Water Is Dripping", "text": "A leaking indoor unit is usually a blocked drain or dirty coil — we clear it and check the cause."},
                {"title": "When the Bill Jumps", "text": "A sudden DEWA rise often means a straining system; a service usually restores efficiency."},
                {"title": "When It Won't Switch On", "text": "We test the power, thermostat, capacitor and controls to find why the unit won't start."},
            ],
            "note": "Regular servicing prevents most of these — a clean system simply runs better and cheaper.",
        },
        "why": {
            "h2": "Why Choose Best Fix for HVAC",
            "intro": "Cooling is too important in Dubai to leave to guesswork. Here's why customers rely on us.",
            "rows": [
                {"icon": "check", "title": "Honest Diagnosis", "text": "We find the real cause and fix the leak, not just top up the gas."},
                {"icon": "pin", "title": "Same-Day Response", "text": "Urgent cooling failures are prioritised, with same-day slots where possible."},
                {"icon": "gear", "title": "All System Types", "text": "Split, ducted, central and cassette systems, repaired and installed."},
                {"icon": "shield", "title": "Efficient & Safe", "text": "Correct servicing keeps cooling strong and your running costs down."},
                {"icon": "users", "title": "Homes & Businesses", "text": "Villas, apartments, offices and managed properties across Dubai."},
                {"icon": "tag", "title": "Clear Pricing", "text": "A clear price before we start — no surprises afterwards."},
            ],
        },
        "steps": {
            "h2": "How It Works",
            "rows": [
                {"n": "1", "title": "Book a Visit", "text": "Tell us the symptom or the service you need and we'll arrange a slot."},
                {"n": "2", "title": "Full Inspection", "text": "We inspect the system to find the true cause of the fault."},
                {"n": "3", "title": "Clear Quote", "text": "You get the diagnosis and price before any work begins."},
                {"n": "4", "title": "Repair or Service", "text": "We carry out the work with genuine parts and proper cleaning."},
                {"n": "5", "title": "Cooling Verified", "text": "We test performance and confirm the system is cooling properly."},
            ],
        },
        "areas": _areas("HVAC Services"),
        "care": {
            "h2": "AC Care Tips for Dubai Homes",
            "rows": [
                {"title": "Clean Filters Often", "text": "In summer, clean or replace filters every few weeks to keep airflow and efficiency up."},
                {"title": "Service Before Peak Heat", "text": "Book a full service before summer so the system is ready for the hardest months."},
                {"title": "Keep Drains Clear", "text": "Clear condensate drains so water doesn't back up and leak from the indoor unit."},
                {"title": "Don't Over-Cool", "text": "A moderate set temperature cools comfortably and costs far less to run."},
                {"title": "Give Units Airflow", "text": "Keep outdoor units clear of dust and obstructions so they can release heat."},
                {"title": "Act on Early Signs", "text": "Weak airflow, odd smells or rising bills mean it's time for a check, not a wait."},
            ],
        },
        "faq_h2": "HVAC Services FAQs",
        "faqs": [
            {"q": "How often should I service my AC in Dubai?", "a": "Because AC runs almost year-round here, we recommend a full service every three to four months, with a lighter filter clean in between — sooner for coastal or heavily used homes."},
            {"q": "My AC isn't cooling well. Does it just need gas?", "a": "Not necessarily. Weak cooling can be a dirty coil, a blocked drain, a compressor or thermostat fault, or a gas leak. We inspect the whole system and fix the real cause."},
            {"q": "Do you offer same-day AC repair?", "a": "Yes. In the Dubai heat a failed AC is urgent, so we prioritise complete cooling failures and leaks and aim to attend the same day."},
            {"q": "Do you install new AC units?", "a": "Yes. We install split, ducted and central systems sized correctly for the space, and we can relocate existing units too."},
            {"q": "Why is my AC leaking water?", "a": "A leaking indoor unit is usually a blocked condensate drain or a dirty coil. We clear it and check the underlying cause so it doesn't return."},
            {"q": "Will servicing lower my DEWA bill?", "a": "Yes. A clean, correctly charged system cools more efficiently, so it draws less power and keeps your bill down."},
        ],
    },

    # ===================================================================== #
    # PLUMBING
    # ===================================================================== #
    "plumbing-services": {
        "meta_title": "Plumbing Services in Dubai | Leaks, Blockages & Repairs — Best Fix",
        "meta_description": (
            "Plumbing services in Dubai by Best Fix — leak repair, blocked drains, "
            "water heaters, taps, toilets and installations for homes and businesses. "
            "Same-day plumbers, clear pricing, tidy work."
        ),
        "breadcrumb": "Plumbing Services",
        "hero": {
            "trustline": "Same-Day Plumbers · Leak & Blockage Experts · Emergency Support",
            "h1_accent": "Plumbing Services in Dubai",
            "h1": "Fixed Fast, Fixed Properly",
            "subheading": "Leaks, blocked drains, water heaters, taps, toilets and installations for homes and businesses.",
            "paras": [
                "A slow drip or a sluggish drain seems minor — until it damages cabinets, "
                "causes mould, or floods through to the neighbour below. Plumbing problems are "
                "cheapest to fix early.",
                "Best Fix provides complete plumbing services across Dubai for apartments, "
                "villas, offices and managed properties. From a dripping tap to a blocked main "
                "or a new bathroom, we diagnose the cause and fix it cleanly.",
                "Our plumbers work tidily, price clearly and leave the job watertight — with "
                "same-day slots for urgent leaks and blockages.",
            ],
            "note": "Emergency support is available for burst pipes, major leaks and overflowing drains.",
            "cta_label": "Book a Plumber",
        },
        "diagnosis": {
            "h2": "Finding the Real Source of the Problem",
            "paras": [
                "Water travels, so the leak you see is often not where the problem is. Our "
                "plumbers trace a leak or blockage back to its source before repairing, so the "
                "fix actually holds.",
                "That means checking joints, seals, pressure and drainage properly — and telling "
                "you honestly whether it's a simple seal, a worn part or something behind the "
                "wall that needs attention.",
            ],
        },
        "services": {
            "h2": "Plumbing Services We Provide",
            "blocks": [
                {"title": "Leak Detection & Repair",
                 "intro": "Dripping taps, leaking pipes, damp patches and hidden leaks traced to "
                          "the source and repaired before they cause damage.",
                 "types_title": "We fix:", "types": ["Dripping taps & mixers", "Leaking pipe joints", "Under-sink leaks", "Concealed / wall leaks", "Water-heater leaks"],
                 "note": "A stain spreading on a wall or ceiling is worth a same-day look before it worsens."},
                {"title": "Blocked Drains & Toilets",
                 "intro": "Slow or blocked sinks, showers, floor drains and toilets cleared "
                          "properly, with the cause checked so it doesn't come straight back.",
                 "types_title": "We clear:", "types": ["Blocked sinks & showers", "Blocked toilets", "Slow floor drains", "Kitchen grease blockages", "Main drain blockages"],
                 "note": "Repeated blockages usually point to a deeper issue — we check, not just plunge."},
                {"title": "Water Heaters",
                 "intro": "No hot water, weak flow, leaks or tripping heaters — repaired, "
                          "serviced or replaced for reliable hot water.",
                 "types_title": "We handle:", "types": ["No hot water", "Leaking heaters", "Thermostat faults", "Descaling & servicing", "New heater installation"],
                 "note": "A heater that trips or leaks should be checked promptly for safety."},
                {"title": "Taps, Toilets & Installations",
                 "intro": "New and faulty taps, mixers, toilets, sinks and bathroom fittings "
                          "installed and sealed cleanly.",
                 "types_title": "We install:", "types": ["Taps & mixers", "Toilets & cisterns", "Sinks & basins", "Showers & hoses", "Bathroom & kitchen fit-outs"],
                 "note": "Proper sealing on new fittings prevents the slow leaks that cause the most damage."},
            ],
        },
        "emergency": {
            "h2": "Emergency Plumbing Support",
            "lead": "Some leaks can't wait — every minute means more damage.",
            "para": "For a burst pipe, a major leak or an overflowing drain, shut off the water "
                    "at the mains where you can and call us. We prioritise these and aim to "
                    "attend the same day.",
            "list_title": "Call us straight away for:",
            "list": ["A burst or badly leaking pipe", "Water coming through a ceiling or wall", "An overflowing or blocked toilet", "A drain backing up into the home", "A leaking water heater"],
            "note": "Knowing where your main stopcock is saves precious time in a real emergency.",
            "explain_title": "On an emergency call we:",
            "explain": ["Stop the water and limit the damage", "Trace the leak or blockage to its source", "Explain the repair and cost before proceeding"],
            "note2": "Fixing a joint or seal early costs a fraction of repairing water-damaged cabinetry and plaster later.",
        },
        "checkfirst": {
            "h2": "Common Plumbing Situations We Handle",
            "rows": [
                {"title": "When a Tap Won't Stop Dripping", "text": "Usually a worn washer or cartridge — a quick fix that saves water and stops the staining."},
                {"title": "When a Drain Runs Slow", "text": "We clear the blockage and check whether it's a one-off or a sign of a deeper issue."},
                {"title": "When There's No Hot Water", "text": "We test the element, thermostat and connections to find why the heater has stopped."},
                {"title": "When You Spot a Damp Patch", "text": "A hidden leak is traced with proper checks before it damages cabinets and walls."},
            ],
            "note": "A quick meter test — note the reading, use no water for an hour, check again — reveals many hidden leaks.",
        },
        "why": {
            "h2": "Why Choose Best Fix for Plumbing",
            "intro": "A tidy, honest plumber who fixes the cause is worth their weight. Here's what you get with us.",
            "rows": [
                {"icon": "check", "title": "Source-First Repairs", "text": "We trace leaks and blockages to the source, so the fix actually lasts."},
                {"icon": "pin", "title": "Same-Day & Emergency", "text": "Urgent leaks and blockages are prioritised, with same-day slots where possible."},
                {"icon": "gear", "title": "Clean, Tidy Work", "text": "We protect your home, work neatly and leave the job watertight."},
                {"icon": "users", "title": "Homes & Businesses", "text": "Apartments, villas, offices and managed properties across Dubai."},
                {"icon": "shield", "title": "Done Properly", "text": "Correct seals, fittings and pressure so problems don't return."},
                {"icon": "tag", "title": "Clear Pricing", "text": "You know the cost before we start — no surprises."},
            ],
        },
        "steps": {
            "h2": "How It Works",
            "rows": [
                {"n": "1", "title": "Book a Visit", "text": "Tell us the problem and we'll arrange a plumber, same day for urgent jobs."},
                {"n": "2", "title": "Trace the Cause", "text": "We find the real source of the leak or blockage before repairing."},
                {"n": "3", "title": "Clear Quote", "text": "You get the fix explained and a clear price before work begins."},
                {"n": "4", "title": "Clean Repair", "text": "We carry out the repair tidily with the right parts and seals."},
                {"n": "5", "title": "Left Watertight", "text": "We test the repair and leave everything clean and dry."},
            ],
        },
        "areas": _areas("Plumbing Services"),
        "care": {
            "h2": "Simple Plumbing Care Tips",
            "rows": [
                {"title": "Check Under Sinks", "text": "Look under sinks and behind the washing machine every couple of months for damp or a musty smell."},
                {"title": "Don't Ignore Drips", "text": "A tap that won't close fully wastes water and often signals a worn washer — an easy early fix."},
                {"title": "Reseal Wet Areas", "text": "Reseal around baths, showers and counters once a year to keep water out of the structure."},
                {"title": "Clear Drains Gently", "text": "Avoid pouring grease down the kitchen sink and use a strainer to catch debris."},
                {"title": "Know Your Stopcock", "text": "Find your main water shut-off now, so you can stop a leak fast when it counts."},
                {"title": "Watch the Meter", "text": "An unexpected jump on your water meter with no usage is a strong sign of a hidden leak."},
            ],
        },
        "faq_h2": "Plumbing Services FAQs",
        "faqs": [
            {"q": "Do you offer same-day plumbing?", "a": "Yes. For urgent leaks and blockages we prioritise the call and aim to attend the same day. Non-urgent jobs are booked to a convenient slot."},
            {"q": "How do you find a hidden leak?", "a": "We trace it to the source using proper checks of joints, seals and pressure rather than opening walls at random, so the repair is targeted and lasts."},
            {"q": "Can you clear a badly blocked drain?", "a": "Yes. We clear blocked sinks, showers, toilets and main drains, and check whether the blockage is a one-off or a sign of a deeper issue."},
            {"q": "Do you install taps, toilets and heaters?", "a": "Yes. We install and replace taps, mixers, toilets, sinks, showers and water heaters, sealed cleanly to prevent leaks."},
            {"q": "My water heater has stopped. Can you help?", "a": "Yes. We diagnose no-hot-water, leaks and tripping heaters, and repair, service or replace as needed."},
            {"q": "Will I get a price before you start?", "a": "Always. Once we've traced the cause we explain the repair and give a clear price before any work begins."},
        ],
    },

    # ===================================================================== #
    # ELECTROMECHANICAL
    # ===================================================================== #
    "electromechanical-services": {
        "meta_title": "Electromechanical Services in Dubai | MEP & Maintenance — Best Fix",
        "meta_description": (
            "Electromechanical (MEP) services in Dubai by Best Fix — combined electrical, "
            "mechanical, HVAC and plumbing installation and maintenance for homes, "
            "offices, retail and managed properties. One trusted team."
        ),
        "breadcrumb": "Electromechanical Services",
        "hero": {
            "trustline": "MEP Installation & Maintenance · One Coordinated Team",
            "h1_accent": "Electromechanical Services in Dubai",
            "h1": "MEP, Handled by One Team",
            "subheading": "Combined electrical, mechanical, HVAC and plumbing work for homes, offices, retail and managed properties.",
            "paras": [
                "Most buildings don't fail one system at a time — a fit-out, a maintenance "
                "contract or a fault often touches electrical, mechanical, HVAC and plumbing "
                "together. Coordinating separate contractors is where things slip.",
                "Best Fix provides electromechanical (MEP) services across Dubai, bringing "
                "electrical, HVAC, plumbing and mechanical work under one coordinated team — "
                "for installation, maintenance and fault-finding.",
                "That means fewer handoffs, one point of contact and work that's planned so the "
                "systems actually work together, cleanly and to standard.",
            ],
            "note": "Ideal for offices, retail units, villas and managed properties needing coordinated MEP work.",
            "cta_label": "Discuss Your Project",
        },
        "diagnosis": {
            "h2": "One Team That Sees the Whole Picture",
            "paras": [
                "When electrical, cooling and plumbing all meet — a new office, a villa "
                "refurbishment, a retail fit-out — the value is in coordination. We assess the "
                "whole scope first so systems are planned together, not patched around each other.",
                "For maintenance, one team that understands every system means faults are "
                "diagnosed faster and nothing falls between contractors.",
            ],
        },
        "services": {
            "h2": "Electromechanical Services We Provide",
            "blocks": [
                {"title": "Electrical Systems",
                 "intro": "Wiring, distribution boards, lighting, power points and fault-finding, "
                          "installed and maintained to DEWA standards.",
                 "types_title": "Includes:", "types": ["Wiring & rewiring", "DB boards & breakers", "Lighting & power points", "Fault-finding", "Testing & certification"],
                 "note": "Delivered as part of a coordinated MEP scope or as standalone electrical work."},
                {"title": "HVAC & Mechanical",
                 "intro": "Air-conditioning, ventilation and mechanical systems installed, "
                          "serviced and repaired for comfort and efficiency.",
                 "types_title": "Includes:", "types": ["AC install & service", "Ventilation", "Ducting", "Exhaust & fresh-air systems", "Preventive maintenance"],
                 "note": "Correctly sized and maintained systems keep running costs down."},
                {"title": "Plumbing & Water Systems",
                 "intro": "Water supply, drainage, heaters and sanitary fittings installed and "
                          "maintained cleanly and to standard.",
                 "types_title": "Includes:", "types": ["Water supply & drainage", "Water heaters", "Pumps", "Sanitary fittings", "Leak & blockage repair"],
                 "note": "Planned alongside electrical and HVAC so everything is coordinated."},
                {"title": "Planned & Preventive Maintenance",
                 "intro": "Scheduled maintenance contracts that keep electrical, HVAC and "
                          "plumbing systems running reliably across a property.",
                 "types_title": "Covers:", "types": ["Scheduled inspections", "Preventive servicing", "Priority call-outs", "Facilities support", "Reporting"],
                 "note": "One contract, one team — ideal for offices, retail and managed properties."},
            ],
        },
        "checkfirst": {
            "h2": "Where Electromechanical Work Helps",
            "rows": [
                {"title": "Office & Retail Fit-Outs", "text": "Electrical, lighting, AC and plumbing planned and installed together for a clean handover."},
                {"title": "Villa Refurbishments", "text": "Coordinated MEP work so cooling, power and water systems fit the new layout."},
                {"title": "Managed Properties", "text": "One maintenance team covering every system across a building or portfolio."},
                {"title": "Recurring Faults", "text": "A team that understands the whole system finds root causes that single trades can miss."},
            ],
            "note": "One point of contact means fewer delays and no gaps between contractors.",
        },
        "why": {
            "h2": "Why Choose Best Fix for MEP",
            "intro": "Coordinated MEP work removes the friction of juggling separate trades. Here's what you get.",
            "rows": [
                {"icon": "users", "title": "One Coordinated Team", "text": "Electrical, HVAC and plumbing under one contact — fewer handoffs."},
                {"icon": "shield", "title": "To Standard", "text": "Work carried out to DEWA and industry standards, safely and cleanly."},
                {"icon": "gear", "title": "Full MEP Scope", "text": "Installation, maintenance and fault-finding across every system."},
                {"icon": "home", "title": "Homes & Commercial", "text": "Villas, offices, retail units and managed properties across Dubai."},
                {"icon": "check", "title": "Planned Properly", "text": "Systems designed to work together, not patched around each other."},
                {"icon": "tag", "title": "Clear Scope & Pricing", "text": "A clear scope and price up front, with tidy delivery."},
            ],
        },
        "steps": {
            "h2": "How It Works",
            "rows": [
                {"n": "1", "title": "Tell Us the Scope", "text": "Share your project or maintenance needs and we'll assess the full picture."},
                {"n": "2", "title": "Survey & Plan", "text": "We survey the site and plan the coordinated MEP works."},
                {"n": "3", "title": "Clear Proposal", "text": "You get a clear scope and price before work begins."},
                {"n": "4", "title": "Coordinated Delivery", "text": "One team delivers electrical, HVAC and plumbing together."},
                {"n": "5", "title": "Tested & Handed Over", "text": "Systems are tested, certified where needed and handed over clean."},
            ],
        },
        "areas": _areas("Electromechanical Services"),
        "care": {
            "h2": "Getting the Most From Your MEP Systems",
            "rows": [
                {"title": "Plan Maintenance", "text": "Scheduled servicing prevents most breakdowns and extends system life."},
                {"title": "Keep One Record", "text": "A single maintenance record across systems makes faults quicker to diagnose."},
                {"title": "Act on Small Signs", "text": "Minor issues in one system often signal a wider problem — worth an early check."},
                {"title": "Size It Right", "text": "Correctly sized AC, power and water systems run more efficiently and cost less."},
                {"title": "Coordinate Changes", "text": "Plan layout changes across all systems together to avoid rework."},
                {"title": "Use One Team", "text": "A single team that knows your building responds faster and misses less."},
            ],
        },
        "faq_h2": "Electromechanical Services FAQs",
        "faqs": [
            {"q": "What are electromechanical (MEP) services?", "a": "MEP covers the mechanical, electrical and plumbing systems in a building — air-conditioning, power, lighting, water and drainage — installed and maintained together as one coordinated scope."},
            {"q": "Do you handle both installation and maintenance?", "a": "Yes. We deliver new MEP installation for fit-outs and refurbishments, and ongoing planned maintenance for homes, offices and managed properties."},
            {"q": "Can you take on office and retail fit-outs?", "a": "Yes. We coordinate electrical, lighting, AC and plumbing for office, retail and commercial fit-outs, delivered by one team."},
            {"q": "Do you offer maintenance contracts?", "a": "Yes. We provide scheduled preventive maintenance with priority call-outs, ideal for managed properties and businesses."},
            {"q": "Is the work done to standard?", "a": "Yes. Electrical work follows DEWA standards, and all systems are installed and tested to the relevant industry requirements."},
            {"q": "Why use one team instead of separate contractors?", "a": "One coordinated team means fewer handoffs, a single point of contact, faster fault diagnosis and systems planned to work together."},
        ],
    },

    # ===================================================================== #
    # SWIMMING POOL
    # ===================================================================== #
    "swimming-pool-services": {
        "meta_title": "Swimming Pool Services in Dubai | Cleaning & Maintenance — Best Fix",
        "meta_description": (
            "Swimming pool services in Dubai by Best Fix — cleaning, chemical balancing, "
            "pump and filter repair, leak detection and equipment maintenance for villas "
            "and communities. Regular and one-off visits."
        ),
        "breadcrumb": "Swimming Pool Services",
        "hero": {
            "trustline": "Cleaning · Chemical Balancing · Equipment Repair",
            "h1_accent": "Swimming Pool Services in Dubai",
            "h1": "Clean, Clear and Balanced",
            "subheading": "Cleaning, chemical balancing, pump and filter repair, leak detection and equipment maintenance.",
            "paras": [
                "A pool in the Dubai climate needs consistent care — heat, dust and heavy use "
                "throw water balance off quickly, and neglected equipment fails when you least "
                "want it to.",
                "Best Fix provides complete swimming pool services across Dubai for villas, "
                "compounds and communities. From regular cleaning and chemical balancing to "
                "pump, filter and leak repairs, we keep your pool safe and swim-ready.",
                "Choose a regular maintenance schedule or a one-off visit — either way you get "
                "clean, balanced water and equipment that's looked after.",
            ],
            "note": "Regular and scheduled maintenance visits available for villas and communities.",
            "cta_label": "Book Pool Service",
        },
        "diagnosis": {
            "h2": "Balanced Water and Healthy Equipment",
            "paras": [
                "Cloudy water, algae or irritated skin usually come down to chemical balance "
                "and filtration — not just more chlorine. We test the water and check the "
                "circulation before adjusting anything.",
                "And because the pump and filter do the real work, we inspect the equipment "
                "too, catching a worn seal or a struggling pump before it becomes a costly "
                "failure.",
            ],
        },
        "services": {
            "h2": "Swimming Pool Services We Provide",
            "blocks": [
                {"title": "Pool Cleaning",
                 "intro": "Skimming, brushing, vacuuming and surface cleaning to keep the water "
                          "and pool clear of debris, dust and algae.",
                 "types_title": "Includes:", "types": ["Surface skimming", "Brushing walls & floor", "Vacuuming", "Basket & skimmer cleaning", "Tile-line cleaning"],
                 "note": "In dusty conditions, regular cleaning keeps filtration working and water clear."},
                {"title": "Chemical Balancing",
                 "intro": "Water testing and balancing — chlorine, pH, alkalinity and stabiliser "
                          "— for safe, clear, comfortable water.",
                 "types_title": "We manage:", "types": ["Chlorine levels", "pH & alkalinity", "Stabiliser", "Algae treatment", "Shock dosing"],
                 "note": "Correct balance protects swimmers, surfaces and equipment alike."},
                {"title": "Pump & Filter Repair",
                 "intro": "Noisy, weak or failed pumps and clogged or leaking filters repaired, "
                          "serviced or replaced to keep the water circulating.",
                 "types_title": "We handle:", "types": ["Pump repair & replacement", "Filter cleaning & repair", "Motor faults", "Seal & gasket leaks", "Backwashing"],
                 "note": "Good circulation is what keeps a pool clear — weak flow is worth checking early."},
                {"title": "Leak Detection & Equipment",
                 "intro": "Unexplained water loss traced and repaired, plus servicing of "
                          "heaters, chlorinators, lights and other pool equipment.",
                 "types_title": "We cover:", "types": ["Leak detection", "Plumbing repairs", "Pool heaters", "Salt chlorinators", "Underwater lighting"],
                 "note": "Persistent water loss beyond evaporation usually means a leak worth tracing."},
            ],
        },
        "checkfirst": {
            "h2": "Common Pool Situations We Handle",
            "rows": [
                {"title": "When Water Turns Cloudy", "text": "We test balance and filtration together rather than just adding chemicals."},
                {"title": "When Algae Appears", "text": "We treat the algae and correct the balance and circulation so it doesn't return."},
                {"title": "When the Pump Is Noisy", "text": "A loud or weak pump is inspected for bearing, seal or motor faults before it fails."},
                {"title": "When the Level Keeps Dropping", "text": "We check for leaks in the pool, plumbing and equipment beyond normal evaporation."},
            ],
            "note": "A regular schedule prevents most of these — steady care keeps water clear and equipment healthy.",
        },
        "why": {
            "h2": "Why Choose Best Fix for Pool Care",
            "intro": "A reliable pool team you don't have to chase is worth a lot. Here's what we offer.",
            "rows": [
                {"icon": "check", "title": "Balanced, Safe Water", "text": "Proper testing and balancing for clear, comfortable, safe water."},
                {"icon": "gear", "title": "Equipment Expertise", "text": "Pumps, filters, heaters and chlorinators serviced and repaired."},
                {"icon": "pin", "title": "Regular or One-Off", "text": "Scheduled maintenance or a single visit — whatever suits you."},
                {"icon": "home", "title": "Villas & Communities", "text": "Private villas, compounds and community pools across Dubai."},
                {"icon": "shield", "title": "Preventive Care", "text": "We catch worn parts and imbalance before they become failures."},
                {"icon": "tag", "title": "Clear Pricing", "text": "Straightforward pricing for visits and repairs."},
            ],
        },
        "steps": {
            "h2": "How It Works",
            "rows": [
                {"n": "1", "title": "Book a Visit", "text": "Choose a regular schedule or a one-off visit and we'll arrange it."},
                {"n": "2", "title": "Test & Inspect", "text": "We test the water and check the pump, filter and equipment."},
                {"n": "3", "title": "Clean & Balance", "text": "We clean the pool and correct the chemical balance."},
                {"n": "4", "title": "Repair as Needed", "text": "Any equipment faults are explained and repaired with clear pricing."},
                {"n": "5", "title": "Swim-Ready", "text": "You're left with clear, balanced, swim-ready water."},
            ],
        },
        "areas": _areas("Swimming Pool Services"),
        "care": {
            "h2": "Pool Care Tips Between Visits",
            "rows": [
                {"title": "Skim Regularly", "text": "Remove leaves and debris often so they don't sink and stain or clog the filter."},
                {"title": "Watch the Water Level", "text": "Keep the level at the skimmer's midpoint so the pump doesn't run dry."},
                {"title": "Rinse After Dust Storms", "text": "Dust settles fast here — a quick clean after a storm keeps filtration efficient."},
                {"title": "Run the Pump Enough", "text": "Adequate daily circulation is what keeps water clear, especially in summer."},
                {"title": "Shower Before Swimming", "text": "Rinsing off reduces the load on your chemicals and keeps balance steadier."},
                {"title": "Don't Over-Chlorinate", "text": "More chlorine isn't the fix for cloudy water — balance and filtration usually are."},
            ],
        },
        "faq_h2": "Swimming Pool Services FAQs",
        "faqs": [
            {"q": "How often should my pool be serviced in Dubai?", "a": "For most villa pools a weekly visit keeps water balanced and clear, given the heat, dust and use. Heavily used or community pools may need more frequent care."},
            {"q": "Why does my pool keep going cloudy?", "a": "Cloudy water usually comes down to chemical balance and filtration rather than a lack of chlorine. We test the water and check circulation to fix the real cause."},
            {"q": "Can you repair my pool pump or filter?", "a": "Yes. We repair and replace pumps and filters, and service motors, seals and gaskets to keep the water circulating properly."},
            {"q": "Do you offer one-off visits?", "a": "Yes. You can book a single clean-and-balance visit or a regular maintenance schedule, whichever suits you."},
            {"q": "My pool loses water. Is it a leak?", "a": "Some loss is normal evaporation in the heat. Persistent drops beyond that usually mean a leak in the pool, plumbing or equipment, which we can trace and repair."},
            {"q": "Do you cover community pools?", "a": "Yes. We maintain private villa pools as well as compound and community pools across Dubai."},
        ],
    },

    # ===================================================================== #
    # PAINTING & CLEANING
    # ===================================================================== #
    "painting-cleaning-services": {
        "meta_title": "Painting & Cleaning Services in Dubai | Best Fix",
        "meta_description": (
            "Painting and deep-cleaning services in Dubai by Best Fix — interior and "
            "exterior painting, wall repairs, and professional deep cleaning for homes, "
            "offices and move-in/out. Clean, tidy, on-time work."
        ),
        "breadcrumb": "Painting & Cleaning Services",
        "hero": {
            "trustline": "Interior & Exterior Painting · Deep Cleaning · Tidy Teams",
            "h1_accent": "Painting & Cleaning Services in Dubai",
            "h1": "A Fresh, Spotless Finish",
            "subheading": "Interior and exterior painting, wall repairs and professional deep cleaning for homes and offices.",
            "paras": [
                "A fresh coat of paint and a proper deep clean transform a space — but only if "
                "the prep is done right and the team works cleanly around your home or office.",
                "Best Fix provides painting and cleaning services across Dubai for apartments, "
                "villas, offices and rental handovers. We prepare surfaces properly, paint "
                "neatly and deep-clean thoroughly, protecting your furniture and floors "
                "throughout.",
                "Whether it's a single room, a whole villa or a move-in/move-out clean, you get "
                "a tidy team, a clear price and a finish you'll actually notice.",
            ],
            "note": "Ideal for repaints, renovations, and move-in / move-out handovers.",
            "cta_label": "Get a Quote",
        },
        "diagnosis": {
            "h2": "The Finish Is in the Preparation",
            "paras": [
                "A good paint job is 80% preparation. We fill cracks, sand, clean and prime "
                "surfaces before painting, so the finish is smooth and lasts — not a quick coat "
                "that peels or shows every flaw underneath.",
                "For cleaning, we work room by room to a checklist so nothing is skipped, and "
                "protect your surfaces and belongings while we work.",
            ],
        },
        "services": {
            "h2": "Painting & Cleaning Services We Provide",
            "blocks": [
                {"title": "Interior Painting",
                 "intro": "Walls, ceilings, rooms and whole apartments repainted with proper "
                          "prep, clean lines and minimal disruption.",
                 "types_title": "Includes:", "types": ["Rooms & apartments", "Walls & ceilings", "Feature walls", "Doors & frames", "Colour changes"],
                 "note": "Furniture and floors are covered and protected throughout the job."},
                {"title": "Exterior & Villa Painting",
                 "intro": "Villa exteriors, boundary walls and facades painted with weather-"
                          "appropriate finishes that stand up to the Dubai sun.",
                 "types_title": "Includes:", "types": ["Villa exteriors", "Boundary walls", "Facades", "Weatherproof coatings", "Gates & railings"],
                 "note": "The right exterior coating protects the surface as well as refreshing the look."},
                {"title": "Wall Repairs & Prep",
                 "intro": "Cracks, dents, flaking paint and damp-damaged plaster repaired and "
                          "prepared so the new finish is smooth and even.",
                 "types_title": "Includes:", "types": ["Crack & dent filling", "Sanding & priming", "Flaking paint removal", "Plaster patch repair", "Surface levelling"],
                 "note": "Skipping prep is why cheap paint jobs fail — we do it properly."},
                {"title": "Deep Cleaning",
                 "intro": "Thorough home and office deep cleaning, plus move-in / move-out "
                          "cleans that leave a property genuinely handover-ready.",
                 "types_title": "Includes:", "types": ["Full home deep clean", "Move-in / move-out", "Kitchen & bathroom", "Office cleaning", "Post-renovation clean"],
                 "note": "A proper deep clean reaches the areas everyday cleaning misses."},
            ],
        },
        "checkfirst": {
            "h2": "When People Call Us",
            "rows": [
                {"title": "Before Moving In", "text": "A fresh repaint and deep clean make a new home feel truly yours before the boxes arrive."},
                {"title": "At Tenancy Handover", "text": "Move-out painting and cleaning help meet handover conditions and protect your deposit."},
                {"title": "After Renovation", "text": "Post-renovation cleaning clears the dust and residue that ordinary cleaning can't."},
                {"title": "For a Refresh", "text": "A repaint and deep clean lift a tired space without a full renovation."},
            ],
            "note": "Every job is planned around your schedule to keep disruption to a minimum.",
        },
        "why": {
            "h2": "Why Choose Best Fix for Painting & Cleaning",
            "intro": "A neat team that respects your space and finishes on time makes all the difference. Here's what you get.",
            "rows": [
                {"icon": "check", "title": "Proper Preparation", "text": "Surfaces are filled, sanded and primed so the finish is smooth and lasts."},
                {"icon": "shield", "title": "Furniture Protected", "text": "We cover and protect your floors and belongings throughout."},
                {"icon": "gear", "title": "Clean Lines & Detail", "text": "Neat cutting-in, even coats and a genuinely tidy finish."},
                {"icon": "home", "title": "Homes & Offices", "text": "Apartments, villas, offices and rental handovers across Dubai."},
                {"icon": "users", "title": "Tidy, Reliable Teams", "text": "Polite teams who turn up on time and clean up after themselves."},
                {"icon": "tag", "title": "Clear Pricing", "text": "A clear quote up front for the whole job."},
            ],
        },
        "steps": {
            "h2": "How It Works",
            "rows": [
                {"n": "1", "title": "Tell Us the Job", "text": "Share the space and what you need — paint, clean, or both."},
                {"n": "2", "title": "Quote & Colours", "text": "We give a clear quote and help with colours and finishes."},
                {"n": "3", "title": "Prep & Protect", "text": "We prepare surfaces and protect your furniture and floors."},
                {"n": "4", "title": "Paint or Clean", "text": "We carry out the work neatly, room by room."},
                {"n": "5", "title": "Tidy Handover", "text": "We clean up and hand back a fresh, spotless space."},
            ],
        },
        "areas": _areas("Painting & Cleaning Services"),
        "care": {
            "h2": "Keeping Your Space Looking Fresh",
            "rows": [
                {"title": "Wipe Marks Early", "text": "Clean scuffs and marks gently and soon, before they set into the paint."},
                {"title": "Ventilate Wet Areas", "text": "Good airflow in bathrooms and kitchens reduces the damp that damages paint."},
                {"title": "Touch Up Small Chips", "text": "Keeping a little leftover paint lets you touch up chips before they spread."},
                {"title": "Deep Clean Seasonally", "text": "A seasonal deep clean keeps dust and grime from building up in hard-to-reach spots."},
                {"title": "Address Damp Fast", "text": "Treat the source of any damp quickly so it doesn't lift or stain fresh paint."},
                {"title": "Protect High-Traffic Walls", "text": "A wipeable finish on hallways and kids' rooms keeps them looking new for longer."},
            ],
        },
        "faq_h2": "Painting & Cleaning FAQs",
        "faqs": [
            {"q": "Do you do both painting and cleaning?", "a": "Yes. We handle interior and exterior painting, wall repairs and professional deep cleaning — separately or together, which is ideal for move-in and move-out."},
            {"q": "How long does painting take?", "a": "It depends on the size and condition of the space. After a quick look we give you a clear timeline along with the quote, and we plan around your schedule."},
            {"q": "Will you protect my furniture?", "a": "Yes. We cover and protect floors, furniture and fittings throughout, and clean up thoroughly once the work is done."},
            {"q": "Do you offer move-in / move-out cleaning?", "a": "Yes. Our move-in and move-out deep cleans leave a property handover-ready and help protect your deposit."},
            {"q": "Can you help choose colours?", "a": "Yes. We're happy to advise on colours and finishes that suit the space and light."},
            {"q": "Do you clean after renovations?", "a": "Yes. Post-renovation cleaning clears the fine dust and residue that ordinary cleaning leaves behind."},
        ],
    },

    # ===================================================================== #
    # FALSE CEILING & PARTITION
    # ===================================================================== #
    "false-ceiling-partition-services": {
        "meta_title": "False Ceiling & Partition Services in Dubai | Gypsum Works — Best Fix",
        "meta_description": (
            "False ceiling and partition services in Dubai by Best Fix — gypsum ceilings, "
            "glass and gypsum partitions, cove lighting and office fit-out for homes and "
            "businesses. Clean lines, on-time delivery."
        ),
        "breadcrumb": "False Ceiling & Partition Services",
        "hero": {
            "trustline": "Gypsum Ceilings · Partitions · Office Fit-Out",
            "h1_accent": "False Ceiling & Partition Services in Dubai",
            "h1": "Clean Lines, Smart Spaces",
            "subheading": "Gypsum ceilings, glass and gypsum partitions, cove lighting and fit-out for homes and offices.",
            "paras": [
                "A well-designed false ceiling or partition changes how a space feels and "
                "works — hiding services, shaping light, and dividing a room without losing "
                "it. Done poorly, though, the joints and lines show.",
                "Best Fix provides false ceiling and partition services across Dubai for homes, "
                "offices and retail units. From gypsum ceilings and cove lighting to glass and "
                "gypsum partitions, we build clean, level, well-finished work.",
                "We plan around your layout, lighting and services, and deliver a smooth, "
                "painted-ready finish on time.",
            ],
            "note": "Ideal for renovations, office fit-outs and reconfiguring homes and workspaces.",
            "cta_label": "Get a Quote",
        },
        "diagnosis": {
            "h2": "Planned Around Your Space and Services",
            "paras": [
                "A ceiling or partition isn't just a surface — it has to work with your "
                "lighting, AC, wiring and layout. We plan the design and framing around those "
                "services first, so nothing has to be opened up later.",
                "That planning is what gives you level ceilings, straight partition lines and "
                "cove lighting that sits right — a finish that looks intentional, not improvised.",
            ],
        },
        "services": {
            "h2": "False Ceiling & Partition Services We Provide",
            "blocks": [
                {"title": "Gypsum False Ceilings",
                 "intro": "Level, well-finished gypsum ceilings that conceal services and shape "
                          "the room, ready for paint.",
                 "types_title": "Includes:", "types": ["Plain gypsum ceilings", "Designed / tiered ceilings", "Cove lighting recesses", "Service concealment", "Ceiling repairs"],
                 "note": "Clean joints and a level finish are what separate a good ceiling from a cheap one."},
                {"title": "Cove & Feature Lighting",
                 "intro": "Recessed cove lighting and feature details built into the ceiling to "
                          "shape light and add depth to a room.",
                 "types_title": "Includes:", "types": ["Cove lighting", "LED strip recesses", "Feature ceilings", "Downlight cut-outs", "Design detailing"],
                 "note": "Integrated lighting turns a plain ceiling into a design feature."},
                {"title": "Partitions",
                 "intro": "Gypsum and glass partitions to divide space, add privacy or create "
                          "rooms — built straight, solid and clean.",
                 "types_title": "Includes:", "types": ["Gypsum partitions", "Glass partitions", "Office cubicles", "Storage / feature walls", "Acoustic partitions"],
                 "note": "The right partition divides a space without making it feel closed in."},
                {"title": "Fit-Out & Finishing",
                 "intro": "Office and retail fit-out work — ceilings, partitions and finishing "
                          "coordinated and delivered ready for paint and handover.",
                 "types_title": "Includes:", "types": ["Office fit-out", "Retail fit-out", "Reception features", "Skimming & finishing", "Snagging"],
                 "note": "We coordinate the ceiling, partitions and services so the fit-out comes together cleanly."},
            ],
        },
        "checkfirst": {
            "h2": "When People Call Us",
            "rows": [
                {"title": "Dividing a Room", "text": "A partition creates a new bedroom, office or storage space without a full rebuild."},
                {"title": "Office Fit-Outs", "text": "Ceilings, partitions and cove lighting delivered together for a clean, professional workspace."},
                {"title": "Concealing Services", "text": "A false ceiling hides wiring, ducting and pipework while shaping the light."},
                {"title": "Refreshing a Design", "text": "A tiered ceiling or cove lighting lifts a plain room without major structural work."},
            ],
            "note": "We plan the framing around your lighting and AC so everything lines up first time.",
        },
        "why": {
            "h2": "Why Choose Best Fix for Ceilings & Partitions",
            "intro": "The difference is in the lines, the levels and the finish. Here's what you get with us.",
            "rows": [
                {"icon": "check", "title": "Level & Clean", "text": "Straight lines, level ceilings and neat joints, ready for paint."},
                {"icon": "gear", "title": "Planned Around Services", "text": "Framing designed around your lighting, AC and wiring."},
                {"icon": "home", "title": "Homes & Offices", "text": "Apartments, villas, offices and retail units across Dubai."},
                {"icon": "users", "title": "Coordinated Fit-Out", "text": "Ceilings, partitions and finishing delivered together."},
                {"icon": "shield", "title": "Solid Build", "text": "Well-framed, durable work — not a flimsy quick job."},
                {"icon": "tag", "title": "Clear Pricing", "text": "A clear quote and timeline before we begin."},
            ],
        },
        "steps": {
            "h2": "How It Works",
            "rows": [
                {"n": "1", "title": "Share Your Idea", "text": "Tell us the space and what you want to achieve."},
                {"n": "2", "title": "Survey & Design", "text": "We survey the site and plan the design around your services."},
                {"n": "3", "title": "Clear Quote", "text": "You get a clear scope, timeline and price before work starts."},
                {"n": "4", "title": "Build & Finish", "text": "We frame, board, finish and skim to a paint-ready standard."},
                {"n": "5", "title": "Clean Handover", "text": "We snag, tidy up and hand over a clean, finished space."},
            ],
        },
        "areas": _areas("False Ceiling & Partition Services"),
        "care": {
            "h2": "Caring for Ceilings & Partitions",
            "rows": [
                {"title": "Fix Leaks Fast", "text": "Water is gypsum's enemy — address any roof or pipe leak quickly to protect the ceiling."},
                {"title": "Watch for Stains", "text": "A spreading stain on a ceiling usually means a leak above worth checking early."},
                {"title": "Handle Fixings Carefully", "text": "Use the right anchors when hanging items so partitions and ceilings aren't damaged."},
                {"title": "Keep Cove Lighting Dust-Free", "text": "Occasionally clear dust from cove recesses so the lighting stays crisp."},
                {"title": "Touch Up Hairline Cracks", "text": "Minor settlement cracks are normal and easy to fill and repaint early."},
                {"title": "Plan Changes Ahead", "text": "Route new wiring or AC before boarding to avoid opening finished ceilings later."},
            ],
        },
        "faq_h2": "False Ceiling & Partition FAQs",
        "faqs": [
            {"q": "What are false ceilings used for?", "a": "A false (gypsum) ceiling conceals wiring, ducting and pipework, shapes the lighting and adds a designed finish, while keeping access to the services above."},
            {"q": "Can you build partitions to divide a room?", "a": "Yes. We build gypsum and glass partitions to create rooms, offices, storage or privacy — straight, solid and neatly finished."},
            {"q": "Do you handle office fit-outs?", "a": "Yes. We deliver coordinated ceilings, partitions, cove lighting and finishing for office and retail fit-outs."},
            {"q": "Is the finish ready for paint?", "a": "Yes. We skim and finish to a smooth, paint-ready standard, and we can arrange painting too."},
            {"q": "Will the work be planned around my lighting and AC?", "a": "Yes. We plan the framing around your lighting, AC and wiring first, so everything lines up and nothing is opened up later."},
            {"q": "How long does it take?", "a": "It depends on the size and design. After a site survey we give a clear timeline along with the quote."},
        ],
    },
}
