const ontology = {
  id: "root",
  name: "Consumer Spending Ontology",
  icon: "🌐",
  description: "Complete classification of credit-based transactions in P2P networks",
  children: [
    {
      id: "2.1",
      name: "Sustenance & Nutrition",
      icon: "🍽️",
      description: "All consumables ingested for survival, pleasure, or social bonding",
      attributes: ["Essential", "Recurring", "Disputable"],
      children: [
        {
          id: "2.1.1",
          name: "Food Acquisition",
          icon: "🛒",
          description: "Raw ingredients and unprepared food items",
          children: [
            { id: "2.1.1.1", name: "Groceries", icon: "🥬", description: "Unprepared raw ingredients, pantry staples, beverages for home consumption" },
            { id: "2.1.1.2", name: "Meal Kits", icon: "📦", description: "Pre-portioned ingredients with preparation instructions" },
            { id: "2.1.1.3", name: "Specialty Foods", icon: "🌿", description: "Dietary-specific items (gluten-free, keto, halal, organic certifications)" }
          ]
        },
        {
          id: "2.1.2",
          name: "Prepared Consumption",
          icon: "🍳",
          description: "Ready-to-eat meals and dining experiences",
          children: [
            { id: "2.1.2.1", name: "Quick Service", icon: "🍔", description: "Fast food, street food, food trucks, grab-and-go" },
            { id: "2.1.2.2", name: "Casual Dining", icon: "🍝", description: "Sit-down restaurants, cafes, diners (check splitting scenarios)" },
            { id: "2.1.2.3", name: "Fine Dining", icon: "🍷", description: "Tasting menus, sommelier services, private dining rooms" },
            { id: "2.1.2.4", name: "Ghost Kitchens", icon: "👻", description: "Delivery-only restaurant concepts" }
          ]
        },
        {
          id: "2.1.3",
          name: "Beverages",
          icon: "🥤",
          description: "Alcoholic and non-alcoholic drinks",
          children: [
            { id: "2.1.3.1", name: "Coffee & Tea", icon: "☕", description: "Specialty coffee shops, bubble tea, afternoon tea services" },
            { id: "2.1.3.2", name: "Alcohol", icon: "🍺", description: "Bars, pubs, wine bars, brewery taprooms, bottle service" },
            { id: "2.1.3.3", name: "Smoothies & Juices", icon: "🧃", description: "Health-focused beverage bars" }
          ]
        },
        {
          id: "2.1.4",
          name: "Subscriptions & Recurring",
          icon: "🔄",
          description: "Regular food delivery services",
          children: [
            { id: "2.1.4.1", name: "Meal Delivery", icon: "🚚", description: "Weekly recipe boxes, prepared meal subscriptions" },
            { id: "2.1.4.2", name: "CSA/Farm Shares", icon: "🚜", description: "Community supported agriculture boxes" }
          ]
        }
      ]
    },
    {
      id: "2.2",
      name: "Shelter & Habitation",
      icon: "🏠",
      description: "Physical space occupancy and modification",
      attributes: ["Essential", "High-Value", "Recurring"],
      children: [
        {
          id: "2.2.1",
          name: "Residential Payments",
          icon: "🔑",
          description: "Primary housing costs",
          children: [
            { id: "2.2.1.1", name: "Rent", icon: "📄", description: "Primary residence, subletting, room rentals, Airbnb splits" },
            { id: "2.2.1.2", name: "Mortgage Contributions", icon: "🏦", description: "Housemate contributions to mortgage payments" },
            { id: "2.2.1.3", name: "Security Deposits", icon: "💰", description: "Move-in costs, last month's rent prepayment" }
          ]
        },
        {
          id: "2.2.2",
          name: "Utilities & Infrastructure",
          icon: "⚡",
          description: "Essential home services",
          children: [
            { id: "2.2.2.1", name: "Electricity", icon: "💡", description: "Grid power, solar buyback credits" },
            { id: "2.2.2.2", name: "Water & Sewer", icon: "💧", description: "Municipal services, well maintenance splits" },
            { id: "2.2.2.3", name: "Gas", icon: "🔥", description: "Natural gas, propane delivery" },
            { id: "2.2.2.4", name: "Trash & Waste", icon: "🗑️", description: "Collection fees, special disposal (electronics, hazardous)" },
            { id: "2.2.2.5", name: "Internet/Broadband", icon: "🌐", description: "Cable, fiber, satellite, mobile hotspots" },
            { id: "2.2.2.6", name: "Telecommunications", icon: "📞", description: "Landline, mobile family plan splits" }
          ]
        },
        {
          id: "2.2.3",
          name: "Maintenance & Supplies",
          icon: "🔧",
          description: "Home upkeep and operational needs",
          children: [
            { id: "2.2.3.1", name: "Cleaning Services", icon: "🧹", description: "Housekeepers, carpet cleaning, window washing" },
            { id: "2.2.3.2", name: "Maintenance", icon: "🛠️", description: "HVAC repair, plumbing, electrical, appliance repair" },
            { id: "2.2.3.3", name: "Supplies", icon: "🧴", description: "Cleaning products, light bulbs, batteries, hardware" },
            { id: "2.2.3.4", name: "Lawn & Garden", icon: "🌱", description: "Landscaping, snow removal, pest control" }
          ]
        },
        {
          id: "2.2.4",
          name: "Furniture & Furnishings",
          icon: "🛋️",
          description: "Home furnishings and decor",
          children: [
            { id: "2.2.4.1", name: "Major Furniture", icon: "🪑", description: "Sofas, beds, dining sets (group purchases)" },
            { id: "2.2.4.2", name: "Appliances", icon: "📺", description: "Refrigerators, washers, small appliances" },
            { id: "2.2.4.3", name: "Decor", icon: "🖼️", description: "Art, rugs, curtains, throw pillows (shared aesthetic purchases)" }
          ]
        }
      ]
    },
    {
      id: "2.3",
      name: "Transportation & Mobility",
      icon: "🚗",
      description: "Movement of persons and goods from origin to destination",
      attributes: ["Essential", "Discretionary", "Variable"],
      children: [
        {
          id: "2.3.1",
          name: "Vehicle Operations",
          icon: "⛽",
          description: "Day-to-day vehicle costs",
          children: [
            { id: "2.3.1.1", name: "Fuel", icon: "🛢️", description: "Gasoline, diesel, electric charging (including supercharging splits)" },
            { id: "2.3.1.2", name: "Maintenance", icon: "🔩", description: "Oil changes, tire rotation, brake service" },
            { id: "2.3.1.3", name: "Repairs", icon: "🧰", description: "Mechanical breakdowns, body work, glass replacement" },
            { id: "2.3.1.4", name: "Insurance", icon: "📋", description: "Premium splits, deductible reimbursements" },
            { id: "2.3.1.5", name: "Parking", icon: "🅿️", description: "Meter fees, garage rentals, parking tickets, valet" }
          ]
        },
        {
          id: "2.3.2",
          name: "Vehicle Acquisition",
          icon: "🚙",
          description: "Vehicle financing and ownership",
          children: [
            { id: "2.3.2.1", name: "Lease Payments", icon: "📑", description: "Monthly lease splits" },
            { id: "2.3.2.2", name: "Loan Payments", icon: "💳", description: "Auto loan contributions" },
            { id: "2.3.2.3", name: "Shared Ownership", icon: "🤝", description: "Fractional ownership arrangements" }
          ]
        },
        {
          id: "2.3.3",
          name: "Alternative Transportation",
          icon: "🚲",
          description: "Non-vehicle mobility options",
          children: [
            { id: "2.3.3.1", name: "Rideshare", icon: "🚕", description: "Uber, Lyft, taxi services (group ride splits)" },
            { id: "2.3.3.2", name: "Public Transit", icon: "🚌", description: "Bus, subway, train, ferry passes and single fares" },
            { id: "2.3.3.3", name: "Micromobility", icon: "🛴", description: "Bike shares, e-scooter rentals, e-bike purchases" },
            { id: "2.3.3.4", name: "Carpooling", icon: "👥", description: "Gas money reimbursements, toll splits" }
          ]
        },
        {
          id: "2.3.4",
          name: "Long-Distance Travel",
          icon: "✈️",
          description: "Inter-city and international transport",
          children: [
            { id: "2.3.4.1", name: "Airfare", icon: "🛫", description: "Commercial flights, charter services, baggage fees" },
            { id: "2.3.4.2", name: "Rail", icon: "🚆", description: "Amtrak, high-speed rail, sleeper cars" },
            { id: "2.3.4.3", name: "Bus", icon: "🚌", description: "Greyhound, Megabus, BoltBus" },
            { id: "2.3.4.4", name: "Sea", icon: "🚢", description: "Ferries, cruises (group cabin bookings)" }
          ]
        }
      ]
    },
    {
      id: "2.4",
      name: "Healthcare & Wellness",
      icon: "⚕️",
      description: "Maintenance and restoration of physical and mental health",
      attributes: ["Essential", "High-Risk", "Protected"],
      children: [
        {
          id: "2.4.1",
          name: "Medical Services",
          icon: "🏥",
          description: "Traditional healthcare provision",
          children: [
            { id: "2.4.1.1", name: "Primary Care", icon: "👨‍⚕️", description: "Doctor visits, annual physicals, vaccinations" },
            { id: "2.4.1.2", name: "Specialist Care", icon: "🫀", description: "Cardiology, dermatology, orthopedics, etc." },
            { id: "2.4.1.3", name: "Emergency Services", icon: "🚑", description: "ER visits, urgent care, ambulance transport" },
            { id: "2.4.1.4", name: "Surgical Procedures", icon: "🔪", description: "Inpatient and outpatient surgeries" },
            { id: "2.4.1.5", name: "Dental", icon: "🦷", description: "Cleanings, fillings, orthodontics, oral surgery" },
            { id: "2.4.1.6", name: "Vision", icon: "👓", description: "Eye exams, glasses, contact lenses, LASIK" }
          ]
        },
        {
          id: "2.4.2",
          name: "Mental Health",
          icon: "🧠",
          description: "Psychological and psychiatric care",
          children: [
            { id: "2.4.2.1", name: "Therapy", icon: "💬", description: "Individual counseling, couples therapy, family therapy" },
            { id: "2.4.2.2", name: "Psychiatry", icon: "💊", description: "Medication management, psychiatric evaluations" },
            { id: "2.4.2.3", name: "Support Services", icon: "🤲", description: "Life coaching, career counseling, support groups" }
          ]
        },
        {
          id: "2.4.3",
          name: "Wellness & Prevention",
          icon: "🧘",
          description: "Proactive health maintenance",
          children: [
            { id: "2.4.3.1", name: "Gym Memberships", icon: "💪", description: "Fitness centers, CrossFit boxes, yoga studios" },
            { id: "2.4.3.2", name: "Personal Training", icon: "🏋️", description: "One-on-one fitness instruction" },
            { id: "2.4.3.3", name: "Alternative Medicine", icon: "🪷", description: "Acupuncture, chiropractic, massage therapy" },
            { id: "2.4.3.4", name: "Nutrition", icon: "🥗", description: "Dietitian services, supplement subscriptions" },
            { id: "2.4.3.5", name: "Spa Services", icon: "🧖", description: "Facials, massages, saunas, wellness retreats" }
          ]
        },
        {
          id: "2.4.4",
          name: "Pharmaceuticals & Supplies",
          icon: "💉",
          description: "Medications and medical equipment",
          children: [
            { id: "2.4.4.1", name: "Prescriptions", icon: "📜", description: "Medication co-pays, full-price medications" },
            { id: "2.4.4.2", name: "Over-the-Counter", icon: "💊", description: "Pain relievers, cold medicine, first aid supplies" },
            { id: "2.4.4.3", name: "Medical Devices", icon: "🏥", description: "CPAP machines, blood glucose monitors, wheelchairs" }
          ]
        }
      ]
    },
    {
      id: "2.5",
      name: "Personal Care & Appearance",
      icon: "💅",
      description: "Grooming, hygiene, and aesthetic presentation",
      attributes: ["Discretionary", "Recurring", "Service-Based"],
      children: [
        {
          id: "2.5.1",
          name: "Hair Services",
          icon: "💇",
          description: "Hair care and styling",
          children: [
            { id: "2.5.1.1", name: "Haircuts", icon: "✂️", description: "Barbershops, salons, trims" },
            { id: "2.5.1.2", name: "Styling", icon: "💁", description: "Blowouts, updos, special occasion styling" },
            { id: "2.5.1.3", name: "Coloring", icon: "🎨", description: "Highlights, balayage, root touch-ups, full color" },
            { id: "2.5.1.4", name: "Treatments", icon: "✨", description: "Keratin, perms, extensions, hair replacement" }
          ]
        },
        {
          id: "2.5.2",
          name: "Nail & Skin Care",
          icon: "💅",
          description: "Beauty and skincare services",
          children: [
            { id: "2.5.2.1", name: "Manicures/Pedicures", icon: "💎", description: "Basic polish, gel, acrylics, dip powder" },
            { id: "2.5.2.2", name: "Waxing", icon: "🪒", description: "Body hair removal services" },
            { id: "2.5.2.3", name: "Skincare Treatments", icon: "🧴", description: "Facials, peels, microdermabrasion" },
            { id: "2.5.2.4", name: "Tanning", icon: "☀️", description: "Spray tans, tanning bed sessions" }
          ]
        },
        {
          id: "2.5.3",
          name: "Personal Hygiene Products",
          icon: "🧼",
          description: "At-home care products",
          children: [
            { id: "2.5.3.1", name: "Cosmetics", icon: "💄", description: "Makeup, skincare products, fragrances" },
            { id: "2.5.3.2", name: "Toiletries", icon: "🪥", description: "Shampoo, soap, deodorant, toothpaste, razors" },
            { id: "2.5.3.3", name: "Grooming Tools", icon: "🪒", description: "Hair dryers, clippers, electric razors" }
          ]
        }
      ]
    },
    {
      id: "2.6",
      name: "Education & Skill Development",
      icon: "📚",
      description: "Knowledge acquisition and credentialing",
      attributes: ["Investment", "Long-Term", "High-Value"],
      children: [
        {
          id: "2.6.1",
          name: "Formal Education",
          icon: "🎓",
          description: "Degree and certificate programs",
          children: [
            { id: "2.6.1.1", name: "Tuition", icon: "🏛️", description: "University, college, trade school payments" },
            { id: "2.6.1.2", name: "Fees", icon: "📋", description: "Lab fees, technology fees, activity fees" },
            { id: "2.6.1.3", name: "Textbooks", icon: "📖", description: "Physical and digital course materials" },
            { id: "2.6.1.4", name: "Student Loans", icon: "💰", description: "Private loan repayments between individuals" }
          ]
        },
        {
          id: "2.6.2",
          name: "Professional Development",
          icon: "💼",
          description: "Career advancement activities",
          children: [
            { id: "2.6.2.1", name: "Certifications", icon: "📜", description: "Exam fees, prep courses (PMP, CPA, AWS, etc.)" },
            { id: "2.6.2.2", name: "Continuing Education", icon: "🔄", description: "License renewal courses, professional training" },
            { id: "2.6.2.3", name: "Conferences", icon: "🎤", description: "Registration fees, workshop fees, professional association dues" }
          ]
        },
        {
          id: "2.6.3",
          name: "Skills & Hobbies",
          icon: "🎯",
          description: "Personal enrichment learning",
          children: [
            { id: "2.6.3.1", name: "Classes", icon: "🎨", description: "Cooking, art, music, language, dance lessons" },
            { id: "2.6.3.2", name: "Tutoring", icon: "👨‍🏫", description: "Academic tutoring, test prep (SAT, LSAT, MCAT)" },
            { id: "2.6.3.3", name: "Workshops", icon: "🔨", description: "One-day intensives, seminars, bootcamps" },
            { id: "2.6.3.4", name: "Online Learning", icon: "💻", description: "Course platforms, subscription learning services" }
          ]
        }
      ]
    },
    {
      id: "2.7",
      name: "Entertainment & Recreation",
      icon: "🎭",
      description: "Leisure activities and amusement",
      attributes: ["Discretionary", "Variable", "Experience-Based"],
      children: [
        {
          id: "2.7.1",
          name: "Live Events",
          icon: "🎫",
          description: "In-person performances and spectacles",
          children: [
            { id: "2.7.1.1", name: "Concerts", icon: "🎸", description: "Music venues, festivals, orchestra performances" },
            { id: "2.7.1.2", name: "Theater", icon: "🎭", description: "Broadway, off-Broadway, community theater, opera" },
            { id: "2.7.1.3", name: "Comedy", icon: "😂", description: "Stand-up shows, improv clubs" },
            { id: "2.7.1.4", name: "Sports Events", icon: "⚽", description: "Professional, collegiate, amateur ticket purchases" },
            { id: "2.7.1.5", name: "Cinema", icon: "🎬", description: "Movie theaters, IMAX, 3D screenings, film festivals" }
          ]
        },
        {
          id: "2.7.2",
          name: "Media & Content",
          icon: "📺",
          description: "Digital entertainment consumption",
          children: [
            { id: "2.7.2.1", name: "Streaming Services", icon: "📱", description: "Netflix, Spotify, Disney+, game passes" },
            { id: "2.7.2.2", name: "Digital Purchases", icon: "💿", description: "Movie rentals, album purchases, e-books" },
            { id: "2.7.2.3", name: "Gaming", icon: "🎮", description: "Video game purchases, DLC, in-game currency, loot boxes" },
            { id: "2.7.2.4", name: "News", icon: "📰", description: "Newspaper subscriptions, magazine subscriptions, paywalled content" }
          ]
        },
        {
          id: "2.7.3",
          name: "Recreation & Hobbies",
          icon: "🎨",
          description: "Active leisure pursuits",
          children: [
            { id: "2.7.3.1", name: "Sports & Outdoors", icon: "⛳", description: "Golf greens fees, ski passes, climbing gym memberships" },
            { id: "2.7.3.2", name: "Gaming", icon: "🎰", description: "Casino gambling, lottery tickets, poker buy-ins, bingo" },
            { id: "2.7.3.3", name: "Collecting", icon: "🏆", description: "Trading cards, stamps, coins, memorabilia purchases" },
            { id: "2.7.3.4", name: "Crafts", icon: "🧶", description: "Art supplies, knitting, model building, scrapbooking" }
          ]
        },
        {
          id: "2.7.4",
          name: "Nightlife",
          icon: "🌃",
          description: "Evening social entertainment",
          children: [
            { id: "2.7.4.1", name: "Cover Charges", icon: "🚪", description: "Nightclub entry fees" },
            { id: "2.7.4.2", name: "Bottle Service", icon: "🍾", description: "VIP table minimums, champagne service" },
            { id: "2.7.4.3", name: "Event Hosting", icon: "🎉", description: "Private party venues, karaoke rooms" }
          ]
        }
      ]
    },
    {
      id: "2.8",
      name: "Retail & Merchandise",
      icon: "🛍️",
      description: "Physical goods acquisition for personal use",
      attributes: ["Discretionary", "Tangible", "Disputable"],
      children: [
        {
          id: "2.8.1",
          name: "Apparel",
          icon: "👕",
          description: "Clothing and accessories",
          children: [
            { id: "2.8.1.1", name: "Clothing", icon: "👔", description: "Everyday wear, formal wear, athletic wear, outerwear" },
            { id: "2.8.1.2", name: "Footwear", icon: "👟", description: "Casual shoes, athletic shoes, formal shoes, boots" },
            { id: "2.8.1.3", name: "Accessories", icon: "👜", description: "Jewelry, watches, handbags, belts, hats, scarves" },
            { id: "2.8.1.4", name: "Alterations", icon: "🪡", description: "Tailoring, hemming, repairs, dry cleaning" }
          ]
        },
        {
          id: "2.8.2",
          name: "Electronics & Technology",
          icon: "💻",
          description: "Digital devices and peripherals",
          children: [
            { id: "2.8.2.1", name: "Computers", icon: "🖥️", description: "Laptops, desktops, tablets, peripherals" },
            { id: "2.8.2.2", name: "Mobile Devices", icon: "📱", description: "Smartphones, smartwatches, e-readers" },
            { id: "2.8.2.3", name: "Audio/Visual", icon: "🎧", description: "TVs, headphones, speakers, cameras, gaming consoles" },
            { id: "2.8.2.4", name: "Smart Home", icon: "🏠", description: "Thermostats, security systems, voice assistants, IoT devices" }
          ]
        },
        {
          id: "2.8.3",
          name: "Household Goods",
          icon: "🏡",
          description: "Home necessities and tools",
          children: [
            { id: "2.8.3.1", name: "Kitchenware", icon: "🍳", description: "Cookware, small appliances, utensils, dinnerware" },
            { id: "2.8.3.2", name: "Bedding", icon: "🛏️", description: "Sheets, comforters, pillows, mattresses" },
            { id: "2.8.3.3", name: "Storage", icon: "📦", description: "Organizers, containers, closet systems" },
            { id: "2.8.3.4", name: "Tools", icon: "🔨", description: "Hand tools, power tools, lawn equipment" }
          ]
        },
        {
          id: "2.8.4",
          name: "Books & Media Physical",
          icon: "📚",
          description: "Tangible media formats",
          children: [
            { id: "2.8.4.1", name: "Books", icon: "📖", description: "Fiction, non-fiction, textbooks, coffee table books" },
            { id: "2.8.4.2", name: "Music", icon: "🎵", description: "Vinyl records, CDs, cassette tapes" },
            { id: "2.8.4.3", name: "Movies", icon: "🎬", description: "DVDs, Blu-rays, 4K UHD discs" }
          ]
        }
      ]
    },
    {
      id: "2.9",
      name: "Travel & Tourism",
      icon: "🌍",
      description: "Temporary relocation for leisure or business",
      attributes: ["Discretionary", "High-Value", "Experience-Based"],
      children: [
        {
          id: "2.9.1",
          name: "Accommodation",
          icon: "🏨",
          description: "Temporary lodging arrangements",
          children: [
            { id: "2.9.1.1", name: "Hotels", icon: "🛎️", description: "Chain hotels, boutique hotels, resorts" },
            { id: "2.9.1.2", name: "Short-Term Rentals", icon: "🏠", description: "Airbnb, VRBO, vacation homes" },
            { id: "2.9.1.3", name: "Hostels", icon: "🛏️", description: "Shared dormitories, private hostel rooms" },
            { id: "2.9.1.4", name: "Alternative", icon: "⛺", description: "Camping fees, RV parks, couchsurfing contributions" }
          ]
        },
        {
          id: "2.9.2",
          name: "Activities & Experiences",
          icon: "🎯",
          description: "Destination entertainment",
          children: [
            { id: "2.9.2.1", name: "Tours", icon: "🚩", description: "Guided walking tours, bus tours, food tours, adventure tours" },
            { id: "2.9.2.2", name: "Attractions", icon: "🎡", description: "Museum tickets, amusement parks, zoos, aquariums, monuments" },
            { id: "2.9.2.3", name: "Excursions", icon: "🚤", description: "Day trips, boat charters, helicopter tours, hot air balloons" },
            { id: "2.9.2.4", name: "Equipment Rental", icon: "⛷️", description: "Ski equipment, snorkeling gear, bikes, cars" }
          ]
        },
        {
          id: "2.9.3",
          name: "Travel Services",
          icon: "✈️",
          description: "Travel planning and protection",
          children: [
            { id: "2.9.3.1", name: "Travel Insurance", icon: "🛡️", description: "Trip cancellation, medical coverage" },
            { id: "2.9.3.2", name: "Travel Agency", icon: "🗺️", description: "Booking fees, concierge services" },
            { id: "2.9.3.3", name: "Visa & Documents", icon: "📋", description: "Passport fees, visa application fees, travel document processing" }
          ]
        }
      ]
    },
    {
      id: "2.10",
      name: "Financial Services & Obligations",
      icon: "💳",
      description: "Money management and legal financial duties",
      attributes: ["Essential", "Non-Disputable", "Priority"],
      children: [
        {
          id: "2.10.1",
          name: "Banking & Credit",
          icon: "🏦",
          description: "Financial institution services",
          children: [
            { id: "2.10.1.1", name: "Interest Payments", icon: "📈", description: "Personal loan interest, credit card interest" },
            { id: "2.10.1.2", name: "Fees", icon: "💸", description: "Late fees, overdraft fees, ATM fees, wire transfer fees" },
            { id: "2.10.1.3", name: "Credit Monitoring", icon: "👁️", description: "Identity protection services, credit score monitoring" }
          ]
        },
        {
          id: "2.10.2",
          name: "Insurance (Non-Health)",
          icon: "🛡️",
          description: "Risk protection coverage",
          children: [
            { id: "2.10.2.1", name: "Property", icon: "🏠", description: "Renters insurance, homeowners insurance (group splits)" },
            { id: "2.10.2.2", name: "Life", icon: "❤️", description: "Term life, whole life premium splits" },
            { id: "2.10.2.3", name: "Disability", icon: "♿", description: "Short-term and long-term disability" },
            { id: "2.10.2.4", name: "Umbrella", icon: "☂️", description: "Excess liability coverage" }
          ]
        },
        {
          id: "2.10.3",
          name: "Legal & Professional",
          icon: "⚖️",
          description: "Professional advisory services",
          children: [
            { id: "2.10.3.1", name: "Legal Fees", icon: "📜", description: "Attorney retainers, court fees, mediation costs, notary services" },
            { id: "2.10.3.2", name: "Accounting", icon: "🧮", description: "Tax preparation, bookkeeping services, audit defense" },
            { id: "2.10.3.3", name: "Financial Planning", icon: "📊", description: "Investment advisor fees, financial coaching" }
          ]
        },
        {
          id: "2.10.4",
          name: "Government Obligations",
          icon: "🏛️",
          description: "Mandatory civic payments",
          children: [
            { id: "2.10.4.1", name: "Taxes", icon: "📋", description: "Property tax splits, income tax preparation payments" },
            { id: "2.10.4.2", name: "Fines", icon: "⚠️", description: "Parking tickets, traffic violations, court fines, late fees" },
            { id: "2.10.4.3", name: "Licenses", icon: "🪪", description: "Driver's license fees, professional licenses, pet licenses" }
          ]
        }
      ]
    },
    {
      id: "2.11",
      name: "Communication & Connectivity",
      icon: "📡",
      description: "Information exchange and digital services",
      attributes: ["Essential", "Recurring", "Digital"],
      children: [
        {
          id: "2.11.1",
          name: "Telecommunications",
          icon: "📞",
          description: "Voice and data transmission services",
          children: [
            { id: "2.11.1.1", name: "Mobile Plans", icon: "📱", description: "Postpaid monthly service, device payment plans, roaming charges" },
            { id: "2.11.1.2", name: "Internet Service", icon: "🌐", description: "Home broadband installation, monthly service fees" },
            { id: "2.11.1.3", name: "VoIP Services", icon: "💻", description: "Skype, Zoom, Google Voice premium features" }
          ]
        },
        {
          id: "2.11.2",
          name: "Software & Digital Tools",
          icon: "🖥️",
          description: "Productivity and utility applications",
          children: [
            { id: "2.11.2.1", name: "Productivity", icon: "✅", description: "Microsoft 365, Google Workspace, Notion, Slack" },
            { id: "2.11.2.2", name: "Creative", icon: "🎨", description: "Adobe Creative Cloud, Canva Pro, Figma" },
            { id: "2.11.2.3", name: "Security", icon: "🔒", description: "VPN services, antivirus software, password managers" },
            { id: "2.11.2.4", name: "Cloud Storage", icon: "☁️", description: "Dropbox, iCloud, Google Drive, AWS storage" }
          ]
        },
        {
          id: "2.11.3",
          name: "Communication Hardware",
          icon: "🔌",
          description: "Physical connectivity equipment",
          children: [
            { id: "2.11.3.1", name: "Devices", icon: "📶", description: "Router purchases, range extenders, signal boosters" },
            { id: "2.11.3.2", name: "Accessories", icon: "🔋", description: "Phone cases, chargers, cables, screen protectors" }
          ]
        }
      ]
    },
    {
      id: "2.12",
      name: "Children & Dependents",
      icon: "👶",
      description: "Care and support of minors or dependent adults",
      attributes: ["Essential", "Recurring", "Priority"],
      children: [
        {
          id: "2.12.1",
          name: "Childcare",
          icon: "🧸",
          description: "Supervision and care services",
          children: [
            { id: "2.12.1.1", name: "Daycare", icon: "🏫", description: "Infant care, toddler programs, after-school care" },
            { id: "2.12.1.2", name: "Babysitting", icon: "👩", description: "Date night sitters, occasional childcare" },
            { id: "2.12.1.3", name: "Nannies", icon: "👨‍👩‍👧", description: "Full-time in-home childcare, nanny shares" },
            { id: "2.12.1.4", name: "Activities", icon: "⚽", description: "Soccer leagues, ballet classes, swim lessons, summer camps" }
          ]
        },
        {
          id: "2.12.2",
          name: "Education & Development",
          icon: "📚",
          description: "Learning support for dependents",
          children: [
            { id: "2.12.2.1", name: "School Tuition", icon: "🏛️", description: "Private school, parochial school, preschool" },
            { id: "2.12.2.2", name: "Supplies", icon: "✏️", description: "Backpacks, lunchboxes, school supplies, uniforms" },
            { id: "2.12.2.3", name: "Tutoring", icon: "📖", description: "Homework help, test prep, special education services" }
          ]
        },
        {
          id: "2.12.3",
          name: "Dependent Support",
          icon: "🤝",
          description: "Care for non-child dependents",
          children: [
            { id: "2.12.3.1", name: "Elder Care", icon: "👴", description: "Adult daycare, home health aides, assisted living contributions" },
            { id: "2.12.3.2", name: "Pet Care", icon: "🐕", description: "Veterinary bills, grooming, boarding, pet sitting, pet food" },
            { id: "2.12.3.3", name: "Plant Care", icon: "🪴", description: "Houseplant purchases, maintenance services (plant sitting)" }
          ]
        }
      ]
    },
    {
      id: "2.13",
      name: "Gifts & Gratuities",
      icon: "🎁",
      description: "Voluntary transfers without expectation of equivalent return",
      attributes: ["Discretionary", "Non-Disputable", "Social"],
      children: [
        {
          id: "2.13.1",
          name: "Social Obligations",
          icon: "💝",
          description: "Expected gift-giving occasions",
          children: [
            { id: "2.13.1.1", name: "Birthday Gifts", icon: "🎂", description: "Friends, family, colleagues" },
            { id: "2.13.1.2", name: "Wedding Gifts", icon: "💒", description: "Cash gifts, registry purchases, shower contributions" },
            { id: "2.13.1.3", name: "Baby Gifts", icon: "🍼", description: "Shower gifts, welcome baby presents" },
            { id: "2.13.1.4", name: "Holiday Gifts", icon: "🎄", description: "Christmas, Hanukkah, Diwali, Eid presents" },
            { id: "2.13.1.5", name: "Graduation", icon: "🎓", description: "Monetary gifts, commemorative items" }
          ]
        },
        {
          id: "2.13.2",
          name: "Tipping & Gratuities",
          icon: "💵",
          description: "Service appreciation payments",
          children: [
            { id: "2.13.2.1", name: "Service Tips", icon: "🍽️", description: "Restaurant servers, bartenders, delivery drivers, hairdressers" },
            { id: "2.13.2.2", name: "Holiday Tipping", icon: "🎁", description: "Building superintendents, mail carriers, regular service providers" },
            { id: "2.13.2.3", name: "Micro-tipping", icon: "⭐", description: "Content creators, live streamers, street performers" }
          ]
        },
        {
          id: "2.13.3",
          name: "Charitable Giving",
          icon: "❤️",
          description: "Philanthropic contributions",
          children: [
            { id: "2.13.3.1", name: "Donations", icon: "🏛️", description: "Religious organizations, nonprofits, political campaigns" },
            { id: "2.13.3.2", name: "Crowdfunding", icon: "🌐", description: "GoFundMe, Kickstarter, Patreon subscriptions" },
            { id: "2.13.3.3", name: "Mutual Aid", icon: "🤲", description: "Direct cash assistance to individuals in need" }
          ]
        }
      ]
    },
    {
      id: "2.14",
      name: "Business & Professional Expenses",
      icon: "💼",
      description: "Costs incurred in pursuit of income generation",
      attributes: ["Reimbursable", "Tax-Deductible", "Documented"],
      children: [
        {
          id: "2.14.1",
          name: "Work-Related Travel",
          icon: "✈️",
          description: "Business mobility costs",
          children: [
            { id: "2.14.1.1", name: "Client Entertainment", icon: "🍸", description: "Business meals, event tickets, golf outings" },
            { id: "2.14.1.2", name: "Conference Travel", icon: "🎤", description: "Flights, hotels, meals while traveling for work" },
            { id: "2.14.1.3", name: "Commuting", icon: "🚗", description: "Parking at office, public transit for work (non-reimbursed)" }
          ]
        },
        {
          id: "2.14.2",
          name: "Office & Supplies",
          icon: "🖇️",
          description: "Workplace necessities",
          children: [
            { id: "2.14.2.1", name: "Coworking Spaces", icon: "🏢", description: "Hot desk memberships, private office rentals" },
            { id: "2.14.2.2", name: "Equipment", icon: "💻", description: "Laptops, monitors, ergonomic accessories (non-reimbursed)" },
            { id: "2.14.2.3", name: "Supplies", icon: "📎", description: "Printer ink, paper, pens, notebooks for work use" }
          ]
        },
        {
          id: "2.14.3",
          name: "Professional Services",
          icon: "🤝",
          description: "Business support services",
          children: [
            { id: "2.14.3.1", name: "Contractors", icon: "👷", description: "Freelance hires, virtual assistants, consultants" },
            { id: "2.14.3.2", name: "Marketing", icon: "📢", description: "Ad spend, promotional materials, website hosting" },
            { id: "2.14.3.3", name: "Dues & Subscriptions", icon: "📰", description: "Professional associations, industry publications" }
          ]
        }
      ]
    },
    {
      id: "2.15",
      name: "Digital & Emerging",
      icon: "🚀",
      description: "New and evolving transaction types",
      attributes: ["Emerging", "Variable", "Speculative"],
      children: [
        {
          id: "2.15.1",
          name: "Cryptocurrency & Digital Assets",
          icon: "₿",
          description: "Blockchain-based value exchange",
          children: [
            { id: "2.15.1.1", name: "NFT Purchases", icon: "🖼️", description: "Digital art, collectibles, virtual real estate" },
            { id: "2.15.1.2", name: "Crypto Trading", icon: "📊", description: "Coin purchases, exchange fees, gas fees" },
            { id: "2.15.1.3", name: "Virtual Goods", icon: "🎮", description: "Game skins, virtual currency, digital gifts" }
          ]
        },
        {
          id: "2.15.2",
          name: "Metaverse & Virtual Worlds",
          icon: "🌐",
          description: "Immersive digital environment transactions",
          children: [
            { id: "2.15.2.1", name: "Virtual Real Estate", icon: "🏠", description: "Land purchases in virtual worlds" },
            { id: "2.15.2.2", name: "Avatar Customization", icon: "👤", description: "Virtual clothing, accessories, appearance upgrades" },
            { id: "2.15.2.3", name: "Virtual Events", icon: "🎪", description: "Concerts, conferences, experiences in virtual spaces" }
          ]
        },
        {
          id: "2.15.3",
          name: "Subscription Economy",
          icon: "🔄",
          description: "Modern recurring payment models",
          children: [
            { id: "2.15.3.1", name: "Box Subscriptions", icon: "📦", description: "Curated monthly product boxes" },
            { id: "2.15.3.2", name: "Membership Communities", icon: "👥", description: "Discord Nitro, Patreon tiers, exclusive access" },
            { id: "2.15.3.3", name: "Usage-Based", icon: "📊", description: "Pay-per-use services, metered billing" }
          ]
        }
      ]
    }
  ]
};