"""Renovation core service — data for the 3-level structure.

Renovation is a core service with sub-services, and two of those sub-services
have their own level-3 services. Everything is rendered with the rich grid
layout of ``service_detail.html`` (banner hero + card grid), so the whole
tree lives in ``SERVICE_PAGES`` and is reachable at flat ``/services/<slug>/``
URLs. The nav hierarchy is driven by ``RENOVATION_SUBLINKS``.

  Renovation
  ├─ Home Renovation
  │   ├─ Office Renovation
  │   ├─ Restaurant Renovation
  │   ├─ Villa Renovation
  │   ├─ Kitchen Renovation
  │   ├─ Bathroom Renovation
  │   └─ Apartment Renovation
  ├─ Interior Design
  └─ Home Exteriors
      ├─ Exterior Design
      └─ Exterior Renovation
"""

_BANNER = "img/hero-team.webp"

# ── nav tree (core slug handled separately; this is the dropdown) ───────────
RENOVATION_SUBLINKS = [
    {"name": "Home Renovation", "slug": "home-renovation", "children": [
        {"name": "Office Renovation", "slug": "office-renovation"},
        {"name": "Restaurant Renovation", "slug": "restaurant-renovation"},
        {"name": "Villa Renovation", "slug": "villa-renovation"},
        {"name": "Kitchen Renovation", "slug": "kitchen-renovation"},
        {"name": "Bathroom Renovation", "slug": "bathroom-renovation"},
        {"name": "Apartment Renovation", "slug": "apartment-renovation"},
    ]},
    {"name": "Interior Design", "slug": "interior-design"},
    {"name": "Home Exteriors", "slug": "home-exteriors", "children": [
        {"name": "Exterior Design", "slug": "exterior-design"},
        {"name": "Exterior Renovation", "slug": "exterior-renovation"},
    ]},
]


def _why(subject):
    return {
        "h2": "Why Choose Best Fix for " + subject,
        "intro": (
            "Renovation only goes smoothly when design, build and finishing are "
            "planned together. Here's what you get with Best Fix."
        ),
        "rows": [
            {"icon": "users", "title": "One Coordinated Team",
             "text": "Design, construction, MEP and finishing under one team — fewer handoffs and one point of contact."},
            {"icon": "check", "title": "Clear Scope & Pricing",
             "text": "A detailed scope and a clear, itemised price agreed before any work begins."},
            {"icon": "clock", "title": "On-Time Delivery",
             "text": "Realistic timelines and steady progress, with the site kept clean and safe throughout."},
            {"icon": "shield", "title": "Quality & Compliance",
             "text": "Work carried out to standard with proper materials and tidy, lasting workmanship."},
            {"icon": "home", "title": "Homes & Commercial",
             "text": "Villas, apartments, offices, retail and restaurants across Dubai."},
            {"icon": "tag", "title": "Turnkey Handover",
             "text": "From the first drawing to the final snag, handed over ready to use."},
        ],
    }


def _page(slug, breadcrumb, h1_accent, h1, subheading, lead, diag_h2, diag,
          services_h2, blocks, faqs, why_subject, meta_title, meta_desc,
          trustline, cta_label="Get a Renovation Quote"):
    return {
        slug: {
            "meta_title": meta_title,
            "meta_description": meta_desc,
            "breadcrumb": breadcrumb,
            "layout": "grid",
            "hero": {
                "trustline": trustline,
                "h1_accent": h1_accent,
                "h1": h1,
                "subheading": subheading,
                "paras": lead,
                "note": "Serving villas, apartments, offices, retail and restaurants across Dubai.",
                "image": _BANNER,
                "image_alt": breadcrumb + " in Dubai — Best Fix",
                "cta_label": cta_label,
            },
            "diagnosis": {"h2": diag_h2, "paras": diag},
            "services": {"h2": services_h2, "blocks": blocks},
            "why": _why(why_subject),
            "faq_h2": breadcrumb + " FAQs",
            "faqs": faqs,
        }
    }


def _card(title, intro, types, icon, slug=None):
    b = {"title": title, "intro": intro, "types_title": "Includes:",
         "types": types, "icon": icon}
    if slug:
        b["slug"] = slug
    return b


RENOVATION_PAGES = {}

# ── CORE: Renovation ───────────────────────────────────────────────────────
RENOVATION_PAGES.update(_page(
    "renovation", "Renovation",
    "Renovation Services in Dubai", "Design, Build & Fit-Out, Done Right",
    "Full renovation, interior design and exterior works for homes and businesses — planned and delivered by one team.",
    [
        "A renovation touches everything at once — layout, finishes, electrics, "
        "plumbing and cooling — and it only runs smoothly when those trades are "
        "planned together rather than juggled separately.",
        "Best Fix delivers complete renovation services across Dubai: interior "
        "remodelling, design and exterior works for villas, apartments, offices, "
        "retail units and restaurants, managed by one coordinated team.",
        "From the first concept and drawing to the final coat of paint and snag "
        "list, you get a clear scope, a clear price and a clean, on-time handover.",
    ],
    "One Team From Concept to Handover",
    [
        "Good renovation starts with a proper survey and a realistic plan — not a "
        "rushed quote. We assess the space, understand how you want to use it, and "
        "plan every trade around a single programme.",
        "Because the same team handles design, construction and finishing, nothing "
        "falls between contractors and the result matches what was drawn.",
    ],
    "What We Renovate",
    [
        _card("Home Renovation",
              "Full and partial home remodelling — kitchens, bathrooms, flooring, "
              "joinery and finishes for villas and apartments.",
              ["Villa & apartment remodelling", "Kitchens & bathrooms", "Flooring & joinery", "Electrical & plumbing", "Painting & finishing"],
              "home", slug="home-renovation"),
        _card("Interior Design",
              "Space planning, materials, lighting and custom joinery that turn a "
              "layout into a finished, liveable interior.",
              ["Space planning", "Colour & materials", "Lighting design", "Custom joinery", "Turnkey fit-out"],
              "ruler", slug="interior-design"),
        _card("Home Exteriors",
              "Facade design and exterior renovation — cladding, rendering, "
              "paving, boundary walls and outdoor living spaces.",
              ["Facade design", "Cladding & rendering", "Paving & driveways", "Boundary walls", "Outdoor lighting"],
              "building", slug="home-exteriors"),
    ],
    [
        {"q": "What types of renovation do you handle?", "a": "We handle full and partial renovations for villas, apartments, offices, retail units and restaurants — including interior remodelling, interior design and exterior works, all under one team."},
        {"q": "Do you manage design and construction together?", "a": "Yes. Design, construction, MEP and finishing are delivered by one coordinated team, so the built result matches the drawings and nothing falls between contractors."},
        {"q": "Will I get a clear price before work starts?", "a": "Yes. After a site survey we provide a detailed, itemised scope and price, so you know exactly what's included before any work begins."},
        {"q": "Can you work in occupied homes or offices?", "a": "Yes. We plan the programme to minimise disruption, keep the site clean and safe, and phase the work where you need to stay in the space."},
        {"q": "Do you handle approvals and permits?", "a": "We advise on the approvals your project needs and coordinate the required documentation so the work stays compliant."},
    ],
    "Renovation",
    "Renovation Services in Dubai | Interior, Design & Exteriors — Best Fix",
    "Renovation services in Dubai by Best Fix — home renovation, interior design and exterior works for villas, apartments, offices, retail and restaurants. One team, clear pricing.",
    "Interior · Design · Exteriors · One Renovation Team",
))

# ── SUB: Home Renovation (has level-3 children) ────────────────────────────
RENOVATION_PAGES.update(_page(
    "home-renovation", "Home Renovation",
    "Home Renovation in Dubai", "Remodelled, Refreshed and Finished",
    "Full and partial home renovation for villas and apartments — and specialist renovation for every kind of space.",
    [
        "Whether it's a tired kitchen, a full villa remodel or a complete "
        "apartment refresh, home renovation works best when one team plans the "
        "layout, trades and finishes together.",
        "Best Fix delivers home renovation across Dubai for villas and apartments, "
        "and specialist renovation for offices, restaurants, kitchens and "
        "bathrooms — each planned around how the space is actually used.",
        "You get a clear scope, honest advice on what's worth doing, and a clean, "
        "on-time handover.",
    ],
    "Planned Around How You Live and Work",
    [
        "Every renovation starts with a survey and a plan. We look at the layout, "
        "the condition of the existing services and how you want to use the space, "
        "then build a programme around it.",
        "From there, one team handles the construction, MEP and finishing so the "
        "result is coordinated and lasting.",
    ],
    "Home Renovation Services We Provide",
    [
        _card("Office Renovation",
              "Workspace fit-out and remodelling — partitions, flooring, lighting "
              "and services planned for how the team works.",
              ["Partitions & layout", "Flooring & ceilings", "Electrical & data", "HVAC & lighting", "Furniture & finishes"],
              "building", slug="office-renovation"),
        _card("Restaurant Renovation",
              "Front and back of house remodelling — kitchens, dining areas, "
              "ventilation and finishes built for daily service.",
              ["Kitchen & servery", "Dining area design", "MEP & ventilation", "Flooring & surfaces", "Lighting & branding"],
              "flame", slug="restaurant-renovation"),
        _card("Villa Renovation",
              "Full and partial villa remodelling — kitchens, bathrooms, flooring, "
              "joinery and finishes to a high standard.",
              ["Full villa remodelling", "Kitchens & bathrooms", "Flooring & joinery", "Electrical & plumbing", "Painting & finishing"],
              "home", slug="villa-renovation"),
        _card("Kitchen Renovation",
              "Complete kitchen upgrades — cabinets, worktops, plumbing, lighting "
              "and finishes designed around the way you cook.",
              ["Cabinets & joinery", "Countertops & splashbacks", "Sink & plumbing", "Electrical & lighting", "Flooring & tiling"],
              "tools", slug="kitchen-renovation"),
        _card("Bathroom Renovation",
              "Full bathroom remodelling — sanitaryware, waterproofing, tiling, "
              "plumbing and ventilation done cleanly and to standard.",
              ["Sanitaryware & fittings", "Waterproofing", "Tiling & flooring", "Plumbing & drainage", "Lighting & ventilation"],
              "droplet", slug="bathroom-renovation"),
        _card("Apartment Renovation",
              "Smart apartment renovation that makes the most of the space — "
              "layout, finishes, kitchen and bathroom upgrades.",
              ["Space planning", "Flooring & ceilings", "Kitchen & bath upgrades", "Electrical & lighting", "Built-in storage"],
              "ruler", slug="apartment-renovation"),
    ],
    [
        {"q": "Do you handle full and partial home renovations?", "a": "Yes. We take on complete villa and apartment remodels as well as single-room projects like a kitchen or bathroom, scoped to your budget and priorities."},
        {"q": "Which spaces do you renovate?", "a": "Villas, apartments, offices, restaurants, kitchens and bathrooms — each with a team that understands how that kind of space is used."},
        {"q": "Can you renovate while we stay in the home?", "a": "Often yes. We phase the work and keep the site clean and safe so you can remain in the property where it's practical."},
        {"q": "How long does a home renovation take?", "a": "It depends on scope — a single bathroom is far quicker than a full villa. After the survey we give you a realistic programme with clear milestones."},
        {"q": "Do you supply materials and finishes?", "a": "Yes. We can supply and install everything from flooring and joinery to sanitaryware and lighting, or work with finishes you've chosen."},
    ],
    "Home Renovation",
    "Home Renovation in Dubai | Villas, Apartments & More — Best Fix",
    "Home renovation in Dubai by Best Fix — villa and apartment remodelling plus office, restaurant, kitchen and bathroom renovation. One team, clear scope, clean handover.",
    "Villas · Apartments · Kitchens · Bathrooms & More",
))

# ── SUB: Interior Design (leaf) ────────────────────────────────────────────
RENOVATION_PAGES.update(_page(
    "interior-design", "Interior Design",
    "Interior Design in Dubai", "Considered, Practical and Beautiful",
    "Space planning, materials, lighting and custom joinery that turn a layout into a finished, liveable interior.",
    [
        "Good interior design is about more than how a space looks — it's about "
        "how it works day to day, how light moves through it and how the finishes "
        "hold up over time.",
        "Best Fix provides interior design across Dubai for homes and commercial "
        "spaces, from the first mood board and space plan to a fully coordinated, "
        "turnkey fit-out.",
        "Because we also build, the design is grounded in what can actually be "
        "delivered — on budget and on time.",
    ],
    "Design That's Built to Be Built",
    [
        "We start by understanding how you want to use the space, then develop a "
        "layout, material palette and lighting scheme that fit both the use and "
        "the budget.",
        "Every design is developed with construction in mind, so what you approve "
        "on screen is what gets delivered on site.",
    ],
    "What Our Interior Design Covers",
    [
        _card("Space Planning", "Layouts that make the most of every square metre and the way you move through the space.", ["Zoning & flow", "Furniture layout", "Storage planning"], "ruler"),
        _card("Colour & Materials", "Coordinated palettes of flooring, wall finishes, surfaces and textures that work together.", ["Material palettes", "Flooring & surfaces", "Wall finishes"], "brush"),
        _card("Lighting Design", "Layered lighting that sets the mood and supports how each area is used.", ["Ambient & task lighting", "Feature lighting", "Controls"], "bulb"),
        _card("Custom Joinery & Furniture", "Bespoke cabinetry, wardrobes and furniture made to fit the space exactly.", ["Wardrobes & cabinetry", "Bespoke furniture", "Feature units"], "tools"),
        _card("3D Visualisation", "Realistic visuals so you can see and approve the design before work begins.", ["3D renders", "Material previews", "Layout options"], "gear"),
        _card("Turnkey Fit-Out", "One team to design and deliver the whole interior, handed over ready to use.", ["Full fit-out", "Project management", "Final styling"], "home"),
    ],
    [
        {"q": "Do you offer design only, or design and build?", "a": "Both. We can provide a standalone interior design package, or design and deliver the full fit-out as one turnkey project."},
        {"q": "Do you provide 3D visuals?", "a": "Yes. We produce realistic 3D renders so you can see the layout, materials and lighting and approve the design before any work starts."},
        {"q": "Can you design commercial interiors?", "a": "Yes. We design homes as well as offices, retail units and restaurants, always around how the space needs to function."},
        {"q": "Do you work with my budget?", "a": "Yes. We develop the design and material choices around a clear budget so the finished result is achievable, not just aspirational."},
        {"q": "Can you design custom joinery and furniture?", "a": "Yes. Bespoke wardrobes, cabinetry and furniture made to fit the space exactly are a core part of what we do."},
    ],
    "Interior Design",
    "Interior Design in Dubai | Space Planning & Fit-Out — Best Fix",
    "Interior design in Dubai by Best Fix — space planning, materials, lighting, custom joinery and 3D visualisation, with a turnkey design-and-build option for homes and businesses.",
    "Space Planning · Materials · Lighting · Fit-Out",
))

# ── SUB: Home Exteriors (has level-3 children) ─────────────────────────────
RENOVATION_PAGES.update(_page(
    "home-exteriors", "Home Exteriors",
    "Home Exteriors in Dubai", "Facades, Finishes and Outdoor Spaces",
    "Exterior design and renovation — facades, cladding, paving, boundary walls and outdoor living, planned and built by one team.",
    [
        "The outside of a property takes the full force of the Dubai climate — sun, "
        "heat and dust — and it's the first thing anyone sees. Exterior work needs "
        "to be both durable and well designed.",
        "Best Fix handles home exteriors across Dubai, from fresh facade design to "
        "full exterior renovation, including cladding, rendering, paving, boundary "
        "walls and outdoor living spaces.",
        "Whether you're refreshing a facade or reworking the whole exterior, one "
        "team plans the design and delivers the build.",
    ],
    "Built for the Dubai Climate",
    [
        "Exterior work only lasts when the right materials and detailing are used "
        "for the conditions. We assess the facade and surroundings first, then plan "
        "finishes that hold up to heat, sun and dust.",
        "Design and construction are handled together, so the finished exterior "
        "looks right and performs well over time.",
    ],
    "Home Exterior Services We Provide",
    [
        _card("Exterior Design",
              "Facade concepts, materials, landscaping and lighting that give the "
              "property a fresh, coordinated look.",
              ["Facade concepts", "Material & colour schemes", "Landscaping layout", "Outdoor lighting", "3D visualisation"],
              "ruler", slug="exterior-design"),
        _card("Exterior Renovation",
              "Facade repair and repaint, cladding, rendering, paving, boundary "
              "walls and outdoor fixtures, built to last.",
              ["Facade repair & repaint", "Cladding & rendering", "Paving & driveways", "Boundary walls & gates", "Outdoor lighting & fixtures"],
              "building", slug="exterior-renovation"),
    ],
    [
        {"q": "What exterior work do you handle?", "a": "Facade design and renovation, cladding, rendering, painting, paving, driveways, boundary walls, gates and outdoor lighting — as design-only or full design-and-build."},
        {"q": "Do you design as well as build exteriors?", "a": "Yes. We develop the facade and landscaping design, then deliver the construction with the same team, so the result matches the concept."},
        {"q": "Will the finishes last in the Dubai climate?", "a": "Yes. We select materials and detailing suited to heat, sun and dust, so facades and outdoor surfaces stay durable and looking good."},
        {"q": "Can you renovate just the facade?", "a": "Yes. We can repair, render and repaint a facade on its own, or take on the whole exterior including paving, walls and outdoor spaces."},
        {"q": "Do you handle outdoor living areas?", "a": "Yes. We design and build outdoor living spaces, lighting and landscaping coordination as part of an exterior project."},
    ],
    "Home Exteriors",
    "Home Exteriors in Dubai | Facades & Exterior Renovation — Best Fix",
    "Home exteriors in Dubai by Best Fix — exterior design and renovation, facades, cladding, rendering, paving, boundary walls and outdoor living, built for the Dubai climate.",
    "Facades · Cladding · Paving · Outdoor Spaces",
))


# ── LEVEL-3 pages (leaf) ───────────────────────────────────────────────────
def _leaf(slug, breadcrumb, h1_accent, h1, subheading, lead0, blocks, faqs,
          meta_title, meta_desc, trustline, diag_h2, diag):
    return _page(
        slug, breadcrumb, h1_accent, h1, subheading,
        lead0, diag_h2, diag,
        "What " + breadcrumb + " Covers", blocks, faqs, breadcrumb,
        meta_title, meta_desc, trustline,
    )


RENOVATION_PAGES.update(_leaf(
    "office-renovation", "Office Renovation",
    "Office Renovation in Dubai", "A Workspace That Works Harder",
    "Office fit-out and remodelling — partitions, flooring, lighting and services planned around how your team works.",
    [
        "An office should support the way people actually work — focus, collaboration "
        "and meetings all need the right space and services.",
        "Best Fix delivers office renovation across Dubai, from a single-floor refresh "
        "to a full fit-out, with partitions, flooring, lighting, HVAC and data planned "
        "as one coordinated project.",
        "We work around your business, phasing the job to keep disruption to a minimum.",
    ],
    [
        _card("Partitions & Layout", "Open-plan, cellular or hybrid layouts with glass and drywall partitions.", ["Glass partitions", "Drywall partitions", "Workspace zoning"], "ruler"),
        _card("Flooring & Ceilings", "Durable flooring and false ceilings that look sharp and handle daily use.", ["Flooring", "False ceilings", "Acoustic treatment"], "home"),
        _card("Electrical & Data", "Power, lighting and structured data cabling planned for a modern office.", ["Power & sockets", "Data cabling", "Lighting circuits"], "bolt"),
        _card("HVAC & Ventilation", "Cooling and fresh-air distribution balanced for comfort across the floor.", ["AC distribution", "Ventilation", "Controls"], "wind"),
        _card("Painting & Finishes", "Clean, branded finishes that present well to staff and visitors.", ["Painting", "Wall finishes", "Branding elements"], "brush"),
        _card("Furniture & Fit-Out", "Workstations, storage and meeting spaces installed and ready to use.", ["Workstations", "Storage", "Meeting rooms"], "tools"),
    ],
    [
        {"q": "Can you renovate our office out of hours?", "a": "Yes. We can work evenings, weekends or in phases to keep your business running while the fit-out is carried out."},
        {"q": "Do you handle MEP as part of an office fit-out?", "a": "Yes. Electrical, data, lighting and HVAC are planned and delivered with the build so the whole office is coordinated."},
        {"q": "Can you match our brand and layout needs?", "a": "Yes. We design the layout, finishes and branding around how your team works and how you want the space to feel."},
        {"q": "Do you supply office furniture?", "a": "We can supply and install workstations, storage and meeting-room furniture, or fit out around furniture you provide."},
    ],
    "Office Renovation in Dubai | Fit-Out & Remodelling — Best Fix",
    "Office renovation in Dubai by Best Fix — partitions, flooring, ceilings, electrical, data, HVAC and furniture, delivered as one coordinated fit-out with minimal disruption.",
    "Partitions · MEP · Finishes · Fit-Out",
    "Fit-Out That Fits How You Work",
    [
        "We start with how your team uses the space, then plan the layout, services "
        "and finishes around it — not the other way round.",
        "One team handles construction, MEP and finishing, so the office is delivered "
        "coordinated and ready to occupy.",
    ],
))

RENOVATION_PAGES.update(_leaf(
    "restaurant-renovation", "Restaurant Renovation",
    "Restaurant Renovation in Dubai", "Built for Service and Atmosphere",
    "Front and back of house remodelling — kitchens, dining areas, ventilation and finishes built for daily service.",
    [
        "A restaurant has to work hard behind the scenes and feel right out front — "
        "and both need to be built to handle constant use.",
        "Best Fix delivers restaurant renovation across Dubai, covering commercial "
        "kitchens, dining areas, MEP, ventilation and finishes as one coordinated "
        "project.",
        "We plan the programme tightly to get you back to service as quickly as "
        "possible.",
    ],
    [
        _card("Kitchen & Servery", "Commercial kitchen layouts, surfaces and services built for throughput.", ["Kitchen layout", "Stainless surfaces", "Servery & pass"], "flame"),
        _card("Dining Area Design", "Seating layouts and finishes that set the mood and maximise covers.", ["Seating layout", "Feature walls", "Finishes"], "ruler"),
        _card("MEP & Ventilation", "Extraction, cooling, gas and drainage designed for a busy kitchen.", ["Kitchen extraction", "AC & ventilation", "Gas & drainage"], "wind"),
        _card("Flooring & Surfaces", "Slip-resistant, hard-wearing flooring and easy-clean surfaces.", ["Slip-resistant flooring", "Wall cladding", "Work surfaces"], "home"),
        _card("Lighting & Ambience", "Layered lighting that works for both service and atmosphere.", ["Ambient lighting", "Feature lighting", "Controls"], "bulb"),
        _card("Branding & Finishes", "Signage, feature finishes and details that carry your brand.", ["Signage", "Feature finishes", "Detailing"], "brush"),
    ],
    [
        {"q": "Do you build commercial kitchens?", "a": "Yes. We deliver commercial kitchen layouts, stainless surfaces, extraction, gas and drainage built to handle daily service."},
        {"q": "Can you handle the ventilation and extraction?", "a": "Yes. Kitchen extraction, fresh air and cooling are designed and installed as part of the renovation."},
        {"q": "How quickly can you turn a restaurant around?", "a": "We plan a tight programme and phase the work where possible to get you back to service as fast as is practical for the scope."},
        {"q": "Can you match our brand and concept?", "a": "Yes. We design the dining area, finishes, lighting and signage around your concept and brand."},
    ],
    "Restaurant Renovation in Dubai | Kitchens & Fit-Out — Best Fix",
    "Restaurant renovation in Dubai by Best Fix — commercial kitchens, dining areas, MEP, ventilation, flooring and branded finishes, delivered as one coordinated fit-out.",
    "Kitchens · Dining · MEP · Finishes",
    "Front and Back of House, Handled Together",
    [
        "We plan the kitchen, dining area and services as one project, so the flow "
        "works from delivery to table.",
        "Durable, easy-clean materials and properly designed MEP keep the space "
        "working service after service.",
    ],
))

RENOVATION_PAGES.update(_leaf(
    "villa-renovation", "Villa Renovation",
    "Villa Renovation in Dubai", "Remodelled to a High Standard",
    "Full and partial villa remodelling — kitchens, bathrooms, flooring, joinery and finishes, all under one team.",
    [
        "A villa renovation is a big undertaking that touches every trade — and it "
        "only runs smoothly when they're coordinated from the start.",
        "Best Fix delivers villa renovation across Dubai, from single-room upgrades "
        "to complete remodels, covering structure, MEP, joinery and finishes.",
        "You get honest advice on what's worth doing, a clear price and a clean, "
        "on-time handover.",
    ],
    [
        _card("Full Villa Remodelling", "Reworking layouts and finishes across the whole villa.", ["Layout changes", "Structural works", "Full finishes"], "home"),
        _card("Kitchens & Bathrooms", "Complete kitchen and bathroom upgrades to a high standard.", ["Kitchen upgrades", "Bathroom upgrades", "Sanitaryware & joinery"], "droplet"),
        _card("Flooring & Joinery", "Quality flooring and bespoke joinery fitted throughout.", ["Flooring", "Wardrobes & cabinetry", "Feature joinery"], "tools"),
        _card("Electrical & Plumbing", "Upgraded, safe electrical and plumbing systems throughout the villa.", ["Rewiring", "Plumbing upgrades", "Lighting"], "bolt"),
        _card("Painting & Finishes", "Clean, lasting paint and wall finishes inside and out.", ["Interior painting", "Wall finishes", "Exterior touch-ups"], "brush"),
        _card("Landscaping Coordination", "Outdoor areas coordinated with the interior renovation.", ["Outdoor spaces", "Paving", "Exterior lighting"], "leaf"),
    ],
    [
        {"q": "Do you handle full villa remodels?", "a": "Yes. We take on complete villa renovations as well as single-room upgrades, coordinating every trade under one team."},
        {"q": "Can you change the layout or do structural work?", "a": "Yes. We can rework layouts and carry out structural changes where required, with the right approvals and engineering."},
        {"q": "Do you upgrade electrical and plumbing?", "a": "Yes. Rewiring, plumbing upgrades and lighting are handled as part of the renovation so the whole villa is brought up to standard."},
        {"q": "Can you coordinate outdoor work too?", "a": "Yes. We coordinate landscaping, paving and exterior finishes with the interior renovation for a consistent result."},
    ],
    "Villa Renovation in Dubai | Full & Partial Remodelling — Best Fix",
    "Villa renovation in Dubai by Best Fix — full and partial remodelling, kitchens, bathrooms, flooring, joinery, electrical, plumbing and finishes under one coordinated team.",
    "Remodelling · Kitchens · Bathrooms · Finishes",
    "Every Trade, One Programme",
    [
        "A full villa remodel needs structure, MEP, joinery and finishes to line up. "
        "We plan them as a single programme so the work flows in the right order.",
        "One team and one point of contact means fewer delays and a result that "
        "matches the plan.",
    ],
))

RENOVATION_PAGES.update(_leaf(
    "kitchen-renovation", "Kitchen Renovation",
    "Kitchen Renovation in Dubai", "Designed Around the Way You Cook",
    "Complete kitchen upgrades — cabinets, worktops, plumbing, lighting and finishes designed around how you use the space.",
    [
        "The kitchen works harder than any other room, so a good renovation has to "
        "balance looks with storage, workflow and durability.",
        "Best Fix delivers kitchen renovation across Dubai — from a fresh set of "
        "cabinets and worktops to a full re-layout with new plumbing, electrics and "
        "finishes.",
        "We plan the space around how you cook and hand it over clean and ready to use.",
    ],
    [
        _card("Cabinets & Joinery", "Bespoke and modular cabinetry that fits the space and your storage needs.", ["Base & wall units", "Tall & pantry units", "Bespoke joinery"], "tools"),
        _card("Countertops & Splashbacks", "Hard-wearing worktops and splashbacks in a range of materials.", ["Quartz & granite", "Solid surfaces", "Splashbacks"], "ruler"),
        _card("Sink & Plumbing", "Sinks, taps and plumbing reworked for the new layout.", ["Sinks & taps", "Water supply", "Drainage"], "droplet"),
        _card("Electrical & Lighting", "Power, appliance circuits and layered kitchen lighting.", ["Appliance circuits", "Task lighting", "Under-cabinet lighting"], "bolt"),
        _card("Flooring & Tiling", "Durable, easy-clean flooring and wall tiling.", ["Floor tiling", "Wall tiling", "Waterproofing"], "home"),
        _card("Painting & Finishing", "Clean paint and finishing to complete the kitchen.", ["Painting", "Finishing", "Snagging"], "brush"),
    ],
    [
        {"q": "Do you supply the kitchen cabinets?", "a": "Yes. We supply and install bespoke or modular cabinetry, worktops and splashbacks, or fit units you've chosen."},
        {"q": "Can you change the kitchen layout?", "a": "Yes. We can rework the layout, including moving plumbing and electrics, to improve workflow and storage."},
        {"q": "How long does a kitchen renovation take?", "a": "Most kitchens are completed within a few weeks depending on scope. We give you a clear programme after the survey."},
        {"q": "Do you handle plumbing and electrics?", "a": "Yes. Sinks, taps, appliance circuits and lighting are all handled as part of the kitchen renovation."},
    ],
    "Kitchen Renovation in Dubai | Cabinets, Worktops & More — Best Fix",
    "Kitchen renovation in Dubai by Best Fix — cabinets, countertops, plumbing, electrical, lighting, tiling and finishing, planned around how you cook and handed over ready to use.",
    "Cabinets · Worktops · Plumbing · Lighting",
    "Storage, Workflow and Finish",
    [
        "A good kitchen balances how it looks with how it works. We plan storage, "
        "workflow and services around how you actually cook.",
        "Cabinets, worktops, plumbing and electrics are coordinated so the finished "
        "kitchen is practical and lasting.",
    ],
))

RENOVATION_PAGES.update(_leaf(
    "bathroom-renovation", "Bathroom Renovation",
    "Bathroom Renovation in Dubai", "Clean, Waterproof and Lasting",
    "Full bathroom remodelling — sanitaryware, waterproofing, tiling, plumbing and ventilation, done cleanly and to standard.",
    [
        "A bathroom renovation lives or dies on the parts you can't see — "
        "waterproofing, plumbing and ventilation — as much as the finishes on top.",
        "Best Fix delivers bathroom renovation across Dubai, handling sanitaryware, "
        "tiling, plumbing, drainage and ventilation as one coordinated job.",
        "We get the hidden work right so the finished bathroom stays clean, dry and "
        "problem-free.",
    ],
    [
        _card("Sanitaryware & Fittings", "WCs, basins, showers, baths and brassware supplied and fitted.", ["WCs & basins", "Showers & baths", "Taps & brassware"], "droplet"),
        _card("Waterproofing", "Proper tanking and waterproofing before tiling — the part that lasts.", ["Tanking", "Wet-area sealing", "Leak prevention"], "shield"),
        _card("Tiling & Flooring", "Wall and floor tiling with a clean, level, watertight finish.", ["Wall tiling", "Floor tiling", "Grouting & sealing"], "ruler"),
        _card("Plumbing & Drainage", "Water supply and drainage reworked for the new layout.", ["Water supply", "Drainage", "Concealed pipework"], "wrench"),
        _card("Lighting & Ventilation", "Damp-safe lighting and extraction that keeps the room dry.", ["Damp-rated lighting", "Extraction", "Ventilation"], "bulb"),
        _card("Vanity & Storage", "Vanity units and storage made to fit the space.", ["Vanity units", "Mirrors & cabinets", "Storage"], "tools"),
    ],
    [
        {"q": "Do you handle waterproofing properly?", "a": "Yes. We tank and waterproof wet areas before tiling — it's the step that prevents leaks and keeps the bathroom problem-free."},
        {"q": "Can you change the bathroom layout?", "a": "Yes. We can move sanitaryware and rework plumbing and drainage to improve the layout."},
        {"q": "Do you supply sanitaryware and tiles?", "a": "Yes. We supply and fit sanitaryware, brassware and tiles, or install items you've selected."},
        {"q": "How long does a bathroom take?", "a": "Most bathrooms are completed within a couple of weeks depending on scope. We confirm a programme after the survey."},
    ],
    "Bathroom Renovation in Dubai | Waterproofing & Tiling — Best Fix",
    "Bathroom renovation in Dubai by Best Fix — sanitaryware, waterproofing, tiling, plumbing, drainage, ventilation and vanities, done cleanly and to standard so it lasts.",
    "Sanitaryware · Waterproofing · Tiling · Plumbing",
    "The Hidden Work Done Right",
    [
        "Waterproofing, plumbing and drainage decide whether a bathroom lasts. We "
        "get these right before any tiling goes on.",
        "With the hidden work done properly, the finishes stay clean and the room "
        "stays dry for years.",
    ],
))

RENOVATION_PAGES.update(_leaf(
    "apartment-renovation", "Apartment Renovation",
    "Apartment Renovation in Dubai", "More From Every Square Metre",
    "Smart apartment renovation — layout, finishes, kitchen and bathroom upgrades that make the most of the space.",
    [
        "Apartments reward clever planning — the right layout and storage can make a "
        "compact space feel far bigger and work far better.",
        "Best Fix delivers apartment renovation across Dubai, from finishes and "
        "storage upgrades to full remodels with new kitchens and bathrooms.",
        "We plan around building rules and access, and keep the work clean and tidy "
        "throughout.",
    ],
    [
        _card("Space Planning", "Layouts and storage that make a compact apartment work harder.", ["Layout changes", "Storage planning", "Zoning"], "ruler"),
        _card("Flooring & Ceilings", "Fresh flooring and ceilings that lift the whole apartment.", ["Flooring", "False ceilings", "Cove lighting"], "home"),
        _card("Kitchen & Bath Upgrades", "Updated kitchens and bathrooms sized for apartment living.", ["Kitchen upgrades", "Bathroom upgrades", "Fittings"], "droplet"),
        _card("Electrical & Lighting", "Refreshed power and layered lighting throughout.", ["Power & sockets", "Lighting", "Smart controls"], "bolt"),
        _card("Painting & Finishes", "Clean paint and wall finishes for a bright, fresh feel.", ["Painting", "Wall finishes", "Detailing"], "brush"),
        _card("Built-In Storage", "Bespoke wardrobes and storage made to fit the space.", ["Wardrobes", "Built-in storage", "Feature units"], "tools"),
    ],
    [
        {"q": "Do you follow building and community rules?", "a": "Yes. We plan the work around your building's renovation rules, working hours and access requirements, and handle the needed approvals."},
        {"q": "Can you make a small apartment feel bigger?", "a": "Yes. Smart layout changes, built-in storage and the right finishes and lighting can make a compact apartment feel much more spacious."},
        {"q": "Do you upgrade kitchens and bathrooms too?", "a": "Yes. Kitchen and bathroom upgrades are a common part of apartment renovations and are handled by the same team."},
        {"q": "Will you keep the work clean and tidy?", "a": "Yes. We protect finished areas, manage waste and keep the apartment and common areas clean throughout the job."},
    ],
    "Apartment Renovation in Dubai | Remodel & Upgrades — Best Fix",
    "Apartment renovation in Dubai by Best Fix — space planning, flooring, ceilings, kitchen and bathroom upgrades, lighting, painting and built-in storage, done clean and tidy.",
    "Layout · Finishes · Kitchens · Storage",
    "Clever Planning for Compact Spaces",
    [
        "In an apartment, the layout and storage make the biggest difference. We plan "
        "both around how you live day to day.",
        "The work is coordinated around building rules and kept clean and tidy from "
        "start to finish.",
    ],
))

RENOVATION_PAGES.update(_leaf(
    "exterior-design", "Exterior Design",
    "Exterior Design in Dubai", "A Fresh, Coordinated Look",
    "Facade concepts, materials, landscaping and lighting that give a property a fresh, coordinated exterior.",
    [
        "The exterior sets the tone for the whole property — and a considered design "
        "ties the facade, landscaping and lighting into one coherent look.",
        "Best Fix provides exterior design across Dubai, developing facade concepts, "
        "material and colour schemes, landscaping layouts and lighting.",
        "Because we also build, the design is grounded in what can be delivered "
        "durably in the Dubai climate.",
    ],
    [
        _card("Facade Concepts", "Fresh facade designs that suit the property and the setting.", ["Facade concepts", "Elevations", "Detailing"], "building"),
        _card("Material & Colour Schemes", "Coordinated materials and colours that hold up outdoors.", ["Material palettes", "Colour schemes", "Cladding options"], "brush"),
        _card("Landscaping Layout", "Outdoor layouts that connect the building to its surroundings.", ["Landscaping layout", "Paving & planting", "Outdoor zones"], "leaf"),
        _card("Lighting Design", "Exterior lighting that adds safety and presence at night.", ["Facade lighting", "Landscape lighting", "Controls"], "bulb"),
        _card("Outdoor Living Spaces", "Terraces, seating and shaded areas designed for the climate.", ["Terraces", "Seating areas", "Shade & pergolas"], "home"),
        _card("3D Visualisation", "Realistic visuals so you can approve the look before work starts.", ["3D renders", "Material previews", "Options"], "gear"),
    ],
    [
        {"q": "Do you provide exterior 3D visuals?", "a": "Yes. We produce realistic renders of the facade, materials and lighting so you can see and approve the design before any work begins."},
        {"q": "Do you design landscaping too?", "a": "Yes. Landscaping layout, paving, planting and outdoor living areas are part of our exterior design work."},
        {"q": "Can you design and build the exterior?", "a": "Yes. We can hand over a design package or deliver the full design-and-build, so the finished exterior matches the concept."},
        {"q": "Will the design suit the Dubai climate?", "a": "Yes. We select materials and detailing suited to heat, sun and dust so the exterior stays durable and looks good."},
    ],
    "Exterior Design in Dubai | Facades & Landscaping — Best Fix",
    "Exterior design in Dubai by Best Fix — facade concepts, material and colour schemes, landscaping, lighting, outdoor living and 3D visualisation, with a design-and-build option.",
    "Facades · Materials · Landscaping · Lighting",
    "Design Grounded in What's Buildable",
    [
        "A strong exterior design ties the facade, landscaping and lighting together. "
        "We develop the concept around the property and its setting.",
        "Every design is developed with construction and the climate in mind, so the "
        "look you approve is the look you get.",
    ],
))

RENOVATION_PAGES.update(_leaf(
    "exterior-renovation", "Exterior Renovation",
    "Exterior Renovation in Dubai", "Restored, Sealed and Refreshed",
    "Facade repair and repaint, cladding, rendering, paving, boundary walls and outdoor fixtures, built to last.",
    [
        "Sun, heat and dust are hard on a building's exterior — paint fades, render "
        "cracks and surfaces wear, and left alone the damage only spreads.",
        "Best Fix delivers exterior renovation across Dubai, from facade repair and "
        "repaint to cladding, rendering, paving, boundary walls and outdoor fixtures.",
        "We use materials and detailing suited to the climate so the refreshed "
        "exterior stays looking good.",
    ],
    [
        _card("Facade Repair & Repaint", "Cracks and wear repaired and the facade repainted to refresh the look.", ["Crack repair", "Surface prep", "Exterior repaint"], "brush"),
        _card("Cladding & Rendering", "New cladding and render for a durable, updated finish.", ["Cladding", "Rendering", "Surface finishes"], "building"),
        _card("Waterproofing", "Exterior waterproofing that protects walls and roofs from damage.", ["Wall waterproofing", "Roof sealing", "Leak prevention"], "shield"),
        _card("Paving & Driveways", "Hard-wearing paving and driveways laid to last.", ["Paving", "Driveways", "Pathways"], "ruler"),
        _card("Boundary Walls & Gates", "Repaired or rebuilt boundary walls, fences and gates.", ["Boundary walls", "Fencing", "Gates"], "home"),
        _card("Outdoor Lighting & Fixtures", "Exterior lighting and fixtures installed and refreshed.", ["Outdoor lighting", "Fixtures", "Power points"], "bolt"),
    ],
    [
        {"q": "Can you repair and repaint just the facade?", "a": "Yes. We repair cracks and surface damage, prepare the facade properly and repaint it, or take on the whole exterior."},
        {"q": "Do you handle exterior waterproofing?", "a": "Yes. Wall and roof waterproofing is part of our exterior renovation work and protects the building from long-term damage."},
        {"q": "Do you lay paving and driveways?", "a": "Yes. We lay hard-wearing paving, driveways and pathways suited to the climate and daily use."},
        {"q": "Will the finish last in the sun and dust?", "a": "Yes. We use materials and detailing chosen for the Dubai climate so the refreshed exterior stays durable and looks good."},
    ],
    "Exterior Renovation in Dubai | Facade, Rendering & Paving — Best Fix",
    "Exterior renovation in Dubai by Best Fix — facade repair and repaint, cladding, rendering, waterproofing, paving, boundary walls and outdoor lighting, built for the climate.",
    "Facades · Rendering · Waterproofing · Paving",
    "Refinished to Handle the Climate",
    [
        "Exterior surfaces take a beating from sun, heat and dust. We repair, seal and "
        "refinish them with materials chosen for the conditions.",
        "Getting the preparation and detailing right is what makes an exterior "
        "renovation last, not just look good on day one.",
    ],
))


# ── per-page uploaded images ───────────────────────────────────────────────
# Villa Renovation: specific banner on the hero, and the same general
# renovation image used on the right of the text+image (diagnosis) section.
# Everything else stays the plumbing-style grid layout.
_VILLA_IMG = ("img/Home renovation, villa renovation, office renovation, "
              "exterior design, interior design.jpg")
RENOVATION_PAGES["villa-renovation"]["hero"]["image"] = _VILLA_IMG
RENOVATION_PAGES["villa-renovation"]["hero"]["image_alt"] = "Villa renovation in Dubai — Best Fix"
RENOVATION_PAGES["villa-renovation"]["diagnosis"]["image"] = _VILLA_IMG
