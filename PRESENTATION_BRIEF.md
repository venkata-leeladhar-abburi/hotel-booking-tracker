# Presentation brief — Hotel price-drop tracker (internal deck)

Hand this file to Claude Code together with the 4 design references (3 images + 1 screen recording). Everything Claude Code needs is here: the slide plan, the facts with their source links, and the design direction.

---

## 1. What to build

- A **single self-contained HTML presentation** (16:9 slides, arrow-key / click navigation, slide counter, print-to-PDF friendly). Premium, editorial, calm — not template-looking.
- **Audience: internal discussion only** (founding team). Not an investor deck: no funding ask, no team slide, no names of people.
- **Every slide is about the product.** Each slide answers one question and leads into the next (flow: problem → users → solution → market → competitors → gaps → product → tech → legal → costs → go-to-market → roadmap → scale).
- **Every slide has a visual**: bento cards, product mock-ups (app screens, WhatsApp chat, admin dashboard), illustrations, diagrams or charts. Text stays short; explain simply.
- **Every number has a source**: a small footnote on the slide with a clickable link (list below), plus a full Sources slide at the end.

### Product name rule
The name is **not decided**. Use the working name **StayWatch** and define it in **one place only** (e.g. `const PRODUCT_NAME = "StayWatch"` in JS, injected into every `[data-name]` element, plus `<title>`). Changing that one value must rename the product across the whole deck.

---

## 2. Design direction (from the references)

| Reference | What to take from it |
|---|---|
| **Screen recording (soft blue bento)** — main style | Light background, rounded bento cards with a soft sky-blue gradient image area on top and title + one-line description below. 3D-feeling floating UI pieces (cards, chips like "141 Orders Today", "24/7 Support", "<1 Response"), glassy icon tiles, subtle depth. Headline mixes light and bold weight: "Not a generic agency. A studio with a **contractual commitment** to performance." |
| **Image 1 (RevenueX, warm sunset glass)** | Use for the **title/hero slide** and section dividers: frosted-glass app window floating over a warm photo-like gradient; serif display headline ("Explore your performance") paired with clean sans UI text. |
| **Image 2 (light grey bento grid)** | Use for feature and tech slides: very light grey cards, big clean titles, short muted description with one **bolded phrase**, small illustrative graphic inside each card (integration logos on arcs, role pills, a "Schedule reports" button). |
| **Image 3 (dark bento)** | Use **once** for the Legal & compliance section: near-black cards, white text, checklist rows with tick boxes, a permissions table (Allowed / Not allowed). |

**Typography (premium):**
- Display / headlines: an editorial serif like **PP Editorial New** or **Canela** (licensed) — free fallback **Instrument Serif**.
- UI / body: a grotesk like **Neue Montreal**, **Satoshi** or **Geist** — free fallback **Geist** or **Inter Tight**.
- Numbers in stats: tabular figures of the sans.
- Ask the user if they want to supply licensed font files; otherwise load the free fallbacks from Google Fonts / Fontsource.

**Colour:** off-white page (#F7F8FA-ish), ink near-black text, sky-blue gradient accent (the recording), one warm accent for "savings" (soft amber/coral), dark section for legal. Keep colour meaningful: blue = product/tech, warm = money saved, grey = neutral.

**Rules:** generous whitespace, 1 idea per slide, max ~40 words of body text per slide, consistent card radius (~20–24px), soft shadows only, no stock-template look, no emoji.

---

## 3. Slide plan (~26 slides)

**Part 1 — The idea**
1. **Title (hero)** — StayWatch + "We watch your hotel price after you book — and tell you when to rebook cheaper." Glass app window over warm gradient (Image 1 style) showing a booking card with a "Price dropped ₹1,400" chip.
2. **The problem** — Hotel prices keep moving after you pay; ~40% of reservations drop before the free-cancellation date; nobody rechecks. Visual: price line dropping after a "Booked" marker. Source: Pruvo/Travolution.
3. **Who faces it** — Bento of 4 personas: families on holiday, pilgrims (Tirupati, Kashi), weekend getaways, small business travellers; all book refundable rooms early.
4. **Our solution in one line** — Add booking → we watch → alert → rebook & save. 4-step horizontal flow with icons.
5. **Where users use it: App + WhatsApp** — Two phones side by side: the StayWatch app (bookings list, "Saved ₹2,700" card, big + button) and the WhatsApp chat (forward screenshot → confirm → alert). Message: same backend, two front doors.
6. **User journey** — Timeline mock: Day 0 booking added → daily checks → Day 9 alert → rebooked → saving recorded → tracking ends at deadline.

**Part 2 — Market & competition**
7. **Market size** — Stat bento: MakeMyTrip sold 43M hotel room nights in FY26 (~1.18 lakh/day); domestic room nights +20.4% (Sep-2026 quarter); 2 lakh+ room nights in a single day (Jan 2026); Indian online travel $12B (2022) → $60B (2030 projection). Each stat with its source link.
8. **Existing solutions** — Logo-style tiles: Onto, Pruvo, DreamCheaper, HotelSlash, Google Hotels price tracking, MakeMyTrip Price Drop Protection.
9. **Competitor deep dive** — Comparison table (where, how users add booking, rebooks for you?, price to user, how they earn). Data in section 4.
10. **Positioning map** — 2×2: axis 1 "Works with any booking app ↔ Only own bookings", axis 2 "Alert only ↔ Automatic refund". Place competitors; show our gap: OTA-neutral + WhatsApp/app + Indian languages.
11. **Drawbacks & risks of the idea** — Bento of 6 risks: free competitors; price-data coverage gaps (coupons/bank offers not visible); exact room matching; works only for free-cancellation bookings; booking sites may push back; trust (users must forward personal booking data). Each with a one-line mitigation.
12. **How we stand out** — App + WhatsApp, works with apps people already use, Telugu/Hindi/English, target-price alert before booking, pay only when you save, affiliate rebook links.

**Part 3 — Product**
13. **MVP features (first 8 weeks)** — Bento grid: phone OTP sign-in; add booking by email forward / screenshot / link / WhatsApp; AI reads booking + user confirms; hotel matching; scheduled price checks; alerts (WhatsApp + push + email); guided rebook + cancel steps; "saved so far" counter; deadline reminders; Razorpay UPI payments.
14. **App screens** — 3 phone mock-ups: Home (tracked bookings + total saved), Add booking (+ button with 4 options), Price-drop alert detail (old vs new price, deadline, Rebook button).
15. **Admin dashboard (internal tool)** — Desktop mock-up (Image 1/2 style). Modules: Users & sign-ups funnel; Bookings tracked (status per booking); Alerts sent + rebook rate; Total ₹ saved; Extraction review queue (low-confidence AI reads); Price-source health (SerpApi success rate, failures); API cost per booking; Payments (Razorpay); User feedback & ratings; Support inbox.
16. **Support playbook** — Bento: response-time targets (e.g. WhatsApp reply < 2 h, urgent deadline issues first); common cases with canned answers (wrong hotel matched, price not found, false alert, refund/fee dispute, cancel-and-rebook help); never ask for card/OTP/MMT passwords; data deletion requests; escalation path; log every case to improve the matcher. Keep it as guidance to finalise, not fixed policy.
17. **Version 2 & later features** — WhatsApp bot with screenshots; target-price alert; price-history chart + "book now or wait"; Gmail/Outlook auto-import; referrals; Telugu/Hindi/Tamil UI; later: auto rebook & refund via own bookings, B2B for travel agents, buses/homestays.

**Part 4 — How we build it**
18. **How it works (architecture)** — Diagram: App / WhatsApp → Backend API → AI extraction → Postgres → Scheduler → Price API (SerpApi) → Compare engine → Notifier (WhatsApp template, push, email) → Admin dashboard reads everything.
19. **Where prices come from** — Explain simply: MakeMyTrip, Goibibo, Booking.com, Agoda send prices to Google Hotels; SerpApi reads Google Hotels for us (property_token → prices per site). MakeMyTrip appears in 52% of sponsored and 70%+ of organic Google Hotels listings in India (Skift). Limits: no coupons/bank offers, some small/OYO-only hotels missing, cheapest room per site. Validation step: test 20 real hotels on the free 250 searches.
20. **Data source options** — Cards: SerpApi (MVP), MakCorps / Apify (backup), Agoda & Booking.com affiliate (earn on rebooks), TBO B2B API (own booking later). Note: Amadeus Self-Service closed 17 July 2026 — don't plan on it.
21. **Tech stack** — Logo-style bento (Image 2 style): Flutter app, Next.js admin, Node.js/NestJS or FastAPI, PostgreSQL + Redis, BullMQ scheduler, Gemini Flash (reading bookings), WhatsApp Cloud API, Firebase push, Razorpay, Cloudflare Email Routing (forwarded emails), DigitalOcean Bangalore hosting. Optional: n8n for the first demo.

**Part 5 — Legal (dark section, Image 3 style)**
22. **Legal & compliance** — Cards: IT Act 2000 Sec 43 (civil damages for unauthorised access/extraction) & Sec 66 (criminal only if dishonest/fraudulent: up to 3 yrs / ₹5 lakh); Indian Contract Act (site terms are a contract); Copyright Act 1957 (compiled data/content); DPDP Act 2023 + Rules 2025 (consent, security, deletion — main obligations from 13 May 2027); WhatsApp policy (no general-purpose AI bots since 15 Jan 2026 — task-specific bots allowed; alerts must be approved utility templates; user messages first).
23. **How price trackers stay legal + our rules** — Case cards: CamelCamelCamel (Amazon's official affiliate API), BuyHatke (extension reads the page the user is viewing + affiliate revenue), hiQ v LinkedIn ($500k judgment + stop scraping after fake accounts/terms breach), Meta v Bright Data (logged-out public data allowed under Meta's terms), Ryanair v Booking.com (scraping behind login; verdict later overturned, still in appeal). Our rules table (Allowed / Not allowed): use SerpApi & affiliate APIs ✓; never log into users' accounts ✗; no fake accounts ✗; no CAPTCHA bypass ✗; send rebooks via affiliate links ✓. Footer: "Not legal advice — get a startup lawyer to review."

**Part 6 — Money**
24. **Business model** — Cards: pay-when-you-save (10–15% of saving), first 3 bookings free, target-price alert (~₹49), affiliate commission on rebooks (Agoda ~4–5%, Booking.com via CJ 4%), later B2B for travel agents.
25. **Monthly costs & unit economics** — Table of tools with current prices (section 5) + "≈ ₹30 cost per tracked booking" vs "≈ ₹150 revenue at 15% of a ₹1,000 saving". MVP total ≈ ₹9,000–10,000/month up to ~250 bookings/month.

**Part 7 — Launch & scale**
26. **Go-to-market in India** — Bento: first 100 users (WhatsApp groups, colleges), peak seasons (Dec–Jan, Sankranti, summer, pilgrimage seasons, long weekends, weddings), Reels in Telugu/Hindi/English ("I saved ₹2,700 after booking"), micro-creators, SEO pages, referral loop.
27. **End-to-end roadmap** — Horizontal timeline with gates: Validate (Nov) → Design & setup (wk 1–2) → Build MVP (wk 3–6) → Closed beta, 30 users (wk 7–8) → 100 users & savings proof (Jan 2027) → App store launch → Own booking engine via TBO (company + GST + TBO approval) → B2B for travel agents → New categories.
28. **Scaling features** — Auto cancel-and-rebook with instant refund; book on StayWatch with built-in price protection; price prediction ("best time to book"); buses (refundable), homestays, packages; travel-agent dashboard; AI trip assistant inside WhatsApp (task-specific).
29. **Metrics we track** — Bookings tracked, % with a drop, avg ₹ saved, alert → rebook rate, false-alert rate (< 5% target), cost per tracked booking, repeat users, support tickets per 100 bookings.
30. **Sources** — Every link below, grouped.

(30 is the max; merge slides if it feels long — e.g. 8+9, 22+23.)

---

## 4. Facts & sources (use exactly these; link each on its slide)

**Problem & competitors**
- ~40% of hotel reservations drop in price after booking; drops up to 67% — Pruvo via Travolution: https://www.travolution.com/news/travel-sectors/accommodation/pruvo-launches-in-the-uk-as-robin-hood-of-the-hotel-industry
- Onto: Bengaluru, launched 22 Oct 2026, $1M pre-seed (Stargazer Fund, White Venture Capital); Price Drop Refund incl. bookings made elsewhere; refunds to original payment method; updates via WhatsApp & app; 1 in 2 bookings got a refund; earns hotel commission — https://onto.travel/ · https://m.thewire.in/article/ptiprnews/former-groww-team-launch-onto-a-customer-first-travel-platform-with-usd-1-million-in-pre-seed-funding/amp · https://www.outlookbusiness.com/spotlight/pr-wire/former-groww-team-launch-onto-a-customer-first-travel-platform-with-usd-1-million-in-pre-seed-funding
- Pruvo: Israel (Haifa), founded 2016, $1.1M seed; forward email to save@pruvo.net, free; B2B rebooking for travel agencies — https://siliconcanals.com/news/this-israeli-travel-tech-startup-scored-e1-03m-seed-funding-from-spain-uk-and-netherlands-investors-amid-coronavirus-impact/ · https://clark.com/travel/pruvo-tracks-hotel-price-drops-after-you-book-and-you-keep-the-savings/ · https://www.capterra.com/p/200420/Pruvo/
- DreamCheaper: Berlin, auto cancel & rebook, charges 20% of savings — https://refinery29.com/en-us/2015/03/83737/dream-cheaper-hotel-booking · https://www.cbinsights.com/compare/dreamcheaper-vs-pruvo
- HotelSlash: US, membership $29.95/yr, tracks & alerts, user rebooks — https://www.businesswire.com/news/home/20230510005295/en/HotelSlash-A-New-Hotel-Booking-Service-That-Provides-Travelers-the-Best-Deals-for-More-Than-1-Million-Hotels-Worldwide-Launches-to-the-Public · https://www.10news.com/online-tool-finds-hotel-discounts-even-after-youve-booked
- Google Hotels: free price-drop email alerts for individual hotels (2026) — https://skift.com/2026/04/17/google-hotel-price-tracking-individual-properties/
- MakeMyTrip Price Drop Protection: flights only, ₹229 domestic / ₹349 international per person — https://www.franchiseindia.com/insights/en/news/makemytrips-newly-launched-price-drop-protection-refunds-flyers-if-fares-drop-after-booking.59819

**Market**
- MakeMyTrip: 43M hotel room nights in FY26; record $10.39B gross bookings — https://quartr.com/events/makemytrip-limited-mmyt-investor-presentation_FGfqaJd6
- Domestic room nights +20.4%, standalone +18.6% (Sep-2026 quarter); 105,000+ properties in 2,080 cities; pilgrimage travel a driver — https://www.marketbeat.com/instant-alerts/transcript-makemytrip-q2-earnings-call-highlights-2026-10-26/
- 200,000+ room nights in a single day (24 Jan 2026 weekend) — https://www.barchart.com/story/news/2038814/makemytrip-q4-earnings-call-highlights
- Indian online travel $12B (2022) → $60B (2030 projection) — https://quartr.com/events/makemytrip-limited-mmyt-q1-2026_FGfq8GIT
- MakeMyTrip in 52% of sponsored and 70%+ of organic Google Hotels listings in India — https://skift.com/2025/01/09/makemytrip-dominates-travel-search-in-india-can-it-hold-on-to-its-lead/

**Data & tech**
- SerpApi Google Hotels: property_token → featured_prices + prices per site, rooms — https://serpapi.com/blog/scrape-hotel-prices-using-python-and-a-simple-api/
- Google: hotel prices come from partners (OTAs, hotels, metasearch) — https://support.google.com/travel/answer/6276008
- MakCorps (200+ sites) — https://www.makcorps.com/blog/?p=3181 · Apify Google Hotels — https://apify.com/kestrel/google-hotels-prices
- TBO: India-strong B2B hotel API; needs agency registration + KYC — https://www.vervotech.com/hub/regional/hotel-api-india/ · https://up17.in/tbo-api-integration
- Amadeus Self-Service shut down 17 July 2026 — https://www.phocuswire.com/amadeus-shut-down-self-service-apis-portal-developers
- Agoda affiliate ~4–5% by volume — https://www.creator-hero.com/fr/blog/agoda-affiliate-program-in-depth-review-pros-and-cons · Booking.com via CJ, 4% on stays — https://www.makeinfluence.com/en/academy/booking-coms-affiliate-program-how-travel-creators-earn-commission

**Legal**
- IT Act Sec 43 / 66, Contract Act — https://lawrato.com/indian-kanoon/civil-law/is-web-scraping-legal-in-india-what-a-business-can-and-cannot-collect-3192 · https://spicyip.com/2013/10/data-extraction-intersection-of-copyright-and-information-technology-laws-in-india.html · https://advocategandhi.com/data-scraping-in-india-legal-perspectives-risks-and-regulatory-framework-explained/
- DPDP Rules 2025 phases (Nov 2025 / Nov 2026 / May 2027) — https://compliancehub.wiki/india-dpdp-consent-manager-november-2026-phase-two-deadline-compliance/
- WhatsApp: general-purpose AI bots banned from 15 Jan 2026; task bots allowed — https://respond.io/blog/whatsapp-general-purpose-chatbots-ban
- CamelCamelCamel uses Amazon Product Advertising API — https://softwareengineeringdaily.com/2019/05/24/camelcamelcamel-amazon-price-tracker-with-daniel-green/
- BuyHatke revenue: affiliate, ads, retailer listings — https://yourstory.com/2013/09/buyhatke-iit-kgp-price-discovery-ecommerce
- hiQ v LinkedIn ($500k judgment, permanent injunction) — https://www.natlawreview.com/article/linkedin-s-data-scraping-battle-hiq-labs-ends-proposed-judgment · https://www.zwillgen.com/alternative-data/hiq-v-linkedin-wrapped-up-web-scraping-lessons-learned/
- Meta v Bright Data (2024) — https://www.fbm.com/technology/publications/major-decision-affects-law-of-scraping-and-online-data-collection-meta-platforms-v-bright-data/
- Ryanair v Booking.com (verdict overturned Jan 2025, appealed) — https://blog.ericgoldman.org/archives/2025/03/court-overturns-a-bad-jury-verdict-against-scraping-ryanair-v-booking-guest-blog-post.htm · https://www.ch-aviation.com/news/156303

---

## 5. Costs (current prices, cite on the cost slide)

| Item | Tool | Price | Source |
|---|---|---|---|
| Hotel prices | SerpApi | Free 250/mo; $25/1k; $75/5k; $150/15k; $275/30k searches | https://toolradar.com/tools/serpapi/pricing |
| Read bookings (AI) | Gemini 3.6 Flash | $0.75 / $3.75 per 1M input/output tokens till 31 Dec 2026; $1.50 / $7.50 from 1 Jan 2027 (< ₹1 per booking) | https://www.chatbase.co/blog/gemini-3-6-flash |
| Forwarded emails | Cloudflare Email Routing | Free, unlimited inbound | https://developers.cloudflare.com/email-service/platform/pricing/ |
| WhatsApp alerts | WhatsApp Cloud API | Utility ≈ ₹0.115 per message (+18% GST) | https://montymobile.com/blogs/whatsapp-business-api-pricing-in-india-inr-rates-gst-and-the-2026-currency-migration-deadline |
| Payments | Razorpay | 2% + 18% GST (≈2.36%); new merchants: no platform fee on first ₹5L for 90 days | https://razorpay.com/blog/razorpay-shopify-payment-gateway-pricing-explained/ · https://www.analyticsinsight.net/amp/story/fintech/top-5-payment-gateways-for-indian-startups-for-2027-pricing-features-and-which-one-wins |
| Server + DB | DigitalOcean (Bangalore) | Droplet from $4–6/mo; managed Postgres from $15/mo | https://kuberns.com/blogs/digitalocean-pricing/ |
| App stores | Google Play / Apple | $25 once / $99 per year | — |

- **MVP monthly total:** ≈ ₹9,000–10,000 for up to ~250 tracked bookings/month (SerpApi $75 plan is the biggest line).
- **Cost per tracked booking:** ~20 price checks ≈ ₹26 + AI & WhatsApp ≈ ₹1 + Razorpay ≈ ₹3.5 → **≈ ₹30**.
- **Revenue per successful saving:** 15% of a ₹1,000 saving = ₹150 (+ affiliate commission if rebooked via our link).

---

## 6. Build notes for Claude Code

1. Start by reading this brief and the 4 reference files; write a short design spec (type scale, colours, card styles, spacing) before any slide.
2. Build the deck shell first (navigation, slide counter, name variable, fonts), then 3 sample slides (hero, a bento slide, the dark legal slide) for the user to approve the look.
3. Then build the rest in order. Mock-ups (phones, WhatsApp chat, admin dashboard) are built in HTML/CSS, not images.
4. After each batch, screenshot the slides in a browser and fix overflow, alignment and contrast.
5. Keep one file (`index.html`) with inline CSS/JS unless fonts need separate files.
