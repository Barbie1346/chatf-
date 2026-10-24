"""Ranked channel desk.

Public figures were read from YouTube's public search results on 24 October 2026
using the WEB client. They are not YouTube Studio analytics, and they are not
7-day, 30-day, or 90-day cohort reports. Subscriber labels and relative ages
("8 days ago") are YouTube's own public labels at retrieval time.

RPM figures are cited only from AIR Media-Tech's Studio study of 300 channels,
May 2025–May 2026. Publisher CPM ranges from vidIQ's 29 June 2026 niche guide
(reviewed 8 October 2026) are stored separately and are not treated as measured
revenue.
"""

from __future__ import annotations

RETRIEVED = "2026-10-24"

MONETIZATION_POINTS = {
    "finance": 16,
    "education": 22,
    "tech": 12,
    "food": 10,
    "fitness": 11,
    "hobby": 8,
    "unverified": 9,
    "transport": 18,
    "craft": 11,
}
VELOCITY_POINTS = {
    "breakout": 25,
    "strong": 18,
    "steady": 12,
    "modest": 8,
    "unknown": 3,
}
COMPETITION_POINTS = {"open": 12, "workable": 16, "crowded": 10, "giant": 6}
POLICY_POINTS = {
    "tutorial": 20,
    "sourced": 14,
    "hobby": 16,
    "food": 15,
    "fitness": 14,
    "craft": 16,
}

MONETIZATION_NOTE = {
    "finance": (
        "AIR Business & Finance median RPM was $2.01 (P25–P75 $0.73–$5.17), "
        "directional because fewer than 10 channels were in the sample, "
        "May 2025–May 2026. vidIQ's editorial guide cites a $15–$22 personal-finance "
        "CPM. That CPM is not a Studio measurement and is not used as revenue."
    ),
    "education": (
        "AIR Education & Science median RPM was $10.22 (P25–P75 $2.31–$19.50), "
        "median Studio CPM $5.91, May 2025–May 2026, 3,595 channel-months."
    ),
    "tech": "AIR Gadgets & Tech median RPM was $2.33 (P25–P75 $0.70–$3.71).",
    "food": "AIR Food & Cooking median RPM was $2.25, directional (fewer than 10 channels).",
    "fitness": "No fitness row in the AIR study. Monetization points stay below education.",
    "hobby": "No hobby row in the AIR study. Points reflect unknown advertiser yield.",
    "unverified": "No matching row in the AIR Studio study. RPM is unmeasured.",
    "transport": "AIR Transport median RPM was $5.69, directional (fewer than 10 channels).",
    "craft": "AIR Crafting & Handmade median RPM was $2.39.",
}

EVIDENCE = {
    "air-rpm": {
        "title": "AIR Media-Tech Studio RPM study",
        "url": "https://air.io/en/air-data-findings/how-much-does-youtube-really-pay-in-2026-real-rpm-data-from-300-channels",
        "retrieved": RETRIEVED,
        "kind": "verified-third-party-studio",
        "detail": (
            "300 channels, every monetized month from May 2025 through May 2026, "
            "3,595 channel-months. All-niche median RPM about $2.30. Education & Science "
            "$10.22. Business & Finance $2.01 and marked directional."
        ),
    },
    "vidiq-niches": {
        "title": "vidIQ: 80 Best YouTube Niches for 2026",
        "url": "https://vidiq.com/blog/post/best-youtube-niches/",
        "retrieved": RETRIEVED,
        "kind": "publisher-editorial",
        "detail": (
            "Updated 29 June 2026, reviewed 8 October 2026. Names personal finance, "
            "AI tutorials, real estate, and senior digital skills as opportunity areas. "
            "CPM bands in that article are editorial, not a Studio extract."
        ),
    },
    "ii-gbrs": {
        "title": "interactive investor Great British Retirement Survey 2026",
        "url": "https://www.ii.co.uk/pensions/iiGBRS/2026-financial-advice-and-education",
        "retrieved": RETRIEVED,
        "kind": "verified-survey",
        "detail": (
            "YouTube was the most used social platform for retirement information. "
            "About 34% of Gen Z, 28% of Millennials, and 15% of Gen X in that survey "
            "used YouTube for it. This is survey incidence, not a view count."
        ),
    },
    "govuk-isa": {
        "title": "GOV.UK ISA allowance and 2027 cash-ISA change",
        "url": "https://www.gov.uk/individual-savings-accounts",
        "retrieved": RETRIEVED,
        "kind": "official",
        "detail": (
            "2026 to 2027 tax year overall ISA maximum is £20,000. From 6 April 2027 "
            "the cash ISA limit for people under 65 falls to £12,000 inside the same "
            "£20,000 overall limit. GOV.UK tax-free savings newsletter 23, September 2026."
        ),
    },
    "medicare-compare": {
        "title": "Medicare.gov Medigap comparison chart",
        "url": "https://www.medicare.gov/health-drug-plans/medigap/basics/compare-plan-benefits",
        "retrieved": RETRIEVED,
        "kind": "official",
        "detail": (
            "2026 out-of-pocket limits on the public chart: Plan K $8,000, Plan L $4,000. "
            "High-deductible Plan F and Plan G: $2,950. Plans K and L also reference a "
            "$283 Part B deductible for 2026."
        ),
    },
    "ypp-inauthentic": {
        "title": "YouTube channel monetization policies",
        "url": "https://support.google.com/youtube/answer/1311392?hl=en",
        "retrieved": RETRIEVED,
        "kind": "official",
        "detail": (
            "Inauthentic content includes generic, repetitive, or template-made videos "
            "and AI personas presented as human experts on health, legal issues, finances, "
            "or politics. Mass-produced channels are ineligible for the Partner Program."
        ),
    },
    "yt-damien": {
        "title": "YouTube public search: Damien Talks Money",
        "url": "https://www.youtube.com/@DamienTalksMoney",
        "retrieved": RETRIEVED,
        "kind": "public-search-snapshot",
        "detail": (
            "Channel label 420k subscribers. 'How to Invest at Every Salary' 377,936 views, "
            "8 days ago, 23:23. 'Is This the Worst Time Ever to Buy a House in the UK?' "
            "1,047,849 views, 3 weeks ago, 17:19. Not a Studio retention report."
        ),
    },
    "yt-james": {
        "title": "YouTube public search: James Shack",
        "url": "https://www.youtube.com/@JamesShack",
        "retrieved": RETRIEVED,
        "kind": "public-search-snapshot",
        "detail": (
            "Channel label 283k subscribers. 'Once You Understand This, You'll Stop Working "
            "Past 57' 2,072,923 views, 1 month ago, 14:59. 'It's boring, but it pays 8.1% "
            "guaranteed for life' 831,417 views, 3 weeks ago, 19:07. "
            "'How Much Can You (Actually) Spend in Retirement with £250k/£500k/£1m?' "
            "313,658 views, 2 months ago, 18:23."
        ),
    },
    "yt-pensioncraft": {
        "title": "YouTube public search: PensionCraft",
        "url": "https://www.youtube.com/@Pensioncraft",
        "retrieved": RETRIEVED,
        "kind": "public-search-snapshot",
        "detail": (
            "Channel label 219k subscribers. 'How I Would Invest £10k, £100k & £1m & What "
            "Changes' 47,818 views, 7 days ago, 17:24. 'Retirement - Annuity vs Drawdown' "
            "48,001 views, 2 weeks ago, 11:58."
        ),
    },
    "yt-toby": {
        "title": "YouTube public search: Toby Newbatt",
        "url": "https://www.youtube.com/@TobyNewbatt",
        "retrieved": RETRIEVED,
        "kind": "public-search-snapshot",
        "detail": (
            "Channel label 203k subscribers. 'The Mortgage Crisis of 2026 is Now Here' "
            "490,063 views, 3 weeks ago, 14:54. 'How To Protect Your Investments From the "
            "Stock Market Crash' 167,826 views, 3 days ago, 15:25. "
            "'Stocks and Shares ISA - Beginners Guide (Updated for 2026)' 43,113 views, "
            "6 months ago, 10:31."
        ),
    },
    "yt-nischa": {
        "title": "YouTube public search: Nischa",
        "url": "https://www.youtube.com/@nischa",
        "retrieved": RETRIEVED,
        "kind": "public-search-snapshot",
        "detail": (
            "Channel label 2.27m subscribers. Recent long videos were below the subscriber "
            "base: 151,199 views in 5 days and 229,808 views in 12 days. An older beginner "
            "video, 'Ex-Banker Explains: How to Invest for Beginners in 2026', showed "
            "1,842,915 views at one year."
        ),
    },
    "yt-beclever": {
        "title": "YouTube public search: Be Clever With Your Cash",
        "url": "https://www.youtube.com/@BeCleverWithYourCash",
        "retrieved": RETRIEVED,
        "kind": "public-search-snapshot",
        "detail": (
            "Channel label 120k subscribers. Recent explainers were 4,955 views in 2 days "
            "and 44,452 views in 3 weeks, mostly 13–18 minutes."
        ),
    },
    "yt-humphrey": {
        "title": "YouTube public search: Humphrey Yang",
        "url": "https://www.youtube.com/@humphrey",
        "retrieved": RETRIEVED,
        "kind": "public-search-snapshot",
        "detail": (
            "Channel label 2.09m subscribers. Four videos inside four weeks, each 15–17 "
            "minutes: 137,109 views in 1 day, 204,573 in 8 days, 332,261 in 3 weeks, "
            "961,448 in 4 weeks ('Every Dollar Milestone From $0 to $1M')."
        ),
    },
    "yt-tina": {
        "title": "YouTube public search: Tina Huang",
        "url": "https://www.youtube.com/@TinaHuang1",
        "retrieved": RETRIEVED,
        "kind": "public-search-snapshot",
        "detail": (
            "Channel label 1.36m subscribers. 'Every Size Local AI In 24 Minutes' "
            "1,753,336 views, 3 weeks ago, 24:23. 'Here's the AI Roadmap You Actually Need' "
            "256,498 views, 4 days ago, 25:32."
        ),
    },
    "yt-matt": {
        "title": "YouTube public search: Matt Wolfe",
        "url": "https://www.youtube.com/@mreflow",
        "retrieved": RETRIEVED,
        "kind": "public-search-snapshot",
        "detail": (
            "Channel label 1.02m subscribers. Weekly AI briefings of 26–31 minutes: "
            "75,169 views in 18 hours, 129,610 in 2 days, 176,751 in 7 days."
        ),
    },
    "yt-leila": {
        "title": "YouTube public search: Leila Gharani",
        "url": "https://www.youtube.com/@LeilaGharani",
        "retrieved": RETRIEVED,
        "kind": "public-search-snapshot",
        "detail": (
            "Channel label 3.09m subscribers. 'Stop Copying Data Between Excel Sheets' "
            "321,927 views, 1 month ago, 10:31. Older beginner tutorials still show "
            "millions of lifetime views. Recent velocity is modest relative to the base."
        ),
    },
    "yt-medicare": {
        "title": "YouTube public search: Medicare School",
        "url": "https://www.youtube.com/@MedicareSchool",
        "retrieved": RETRIEVED,
        "kind": "public-search-snapshot",
        "detail": (
            "Channel label 375k subscribers. 'The Only Medicare Plan With a 99% "
            "Satisfaction Rate' 335,240 views, 6 months ago, 24:03. A ranking video "
            "showed 115,929 views at 5 months. No 7-day breakout was in the snapshot."
        ),
    },
    "yt-ken": {
        "title": "YouTube public search: Ken McElroy",
        "url": "https://www.youtube.com/@KenMcElroy",
        "retrieved": RETRIEVED,
        "kind": "public-search-snapshot",
        "detail": (
            "Channel label 528k subscribers. 'Real Estate Just Crashed 50%. Here's My Move' "
            "72,687 views, 2 weeks ago, 16:14."
        ),
    },
    "yt-sorted": {
        "title": "YouTube public search: Sorted Food",
        "url": "https://www.youtube.com/@SortedFood",
        "retrieved": RETRIEVED,
        "kind": "public-search-snapshot",
        "detail": (
            "Channel label 3.01m subscribers. Challenge episodes of 17–24 minutes drew "
            "364,432 views in 2 days and 579,341 in 4 days. That format depends on a "
            "resident cast. It is reference demand, not a format to reproduce."
        ),
    },
    "yt-senior": {
        "title": "YouTube public search: smartphone tutorials for seniors",
        "url": "https://www.youtube.com/results?search_query=smartphone+tutorial+for+seniors",
        "retrieved": RETRIEVED,
        "kind": "public-search-snapshot",
        "detail": (
            "Recent long tutorials on the first page were small: 7,681 views at 1 year "
            "and 8,850 views at 1 year. 'iPhone Basics for Seniors' showed 294,366 views "
            "at 2 years. Thin current supply, not proof of rising search volume."
        ),
    },
    "yt-homeschool": {
        "title": "YouTube public search: homeschool curriculum",
        "url": "https://www.youtube.com/results?search_query=homeschool+curriculum",
        "retrieved": RETRIEVED,
        "kind": "public-search-snapshot",
        "detail": (
            "Recent parent videos on the first page were 6,005 to 33,337 views, "
            "the largest of those at 6 months. Supply looks thin. Demand volume was "
            "not measured."
        ),
    },
    "yt-aqua": {
        "title": "YouTube public search: MJ Aquascaping",
        "url": "https://www.youtube.com/@MJAquascaping",
        "retrieved": RETRIEVED,
        "kind": "public-search-snapshot",
        "detail": (
            "Channel label 270k subscribers. Videos across two weeks showed 37,923 to "
            "70,437 views, lengths 12–33 minutes plus one 113-minute build."
        ),
    },
    "yt-keys": {
        "title": "YouTube public search: mechanical keyboards",
        "url": "https://www.youtube.com/results?search_query=mechanical+keyboard+review",
        "retrieved": RETRIEVED,
        "kind": "public-search-snapshot",
        "detail": (
            "Switch and Click videos showed 412,269 views at 6 months and 537,286 at "
            "4 months. Subscriber count for that channel was not in the payload, so "
            "views per subscriber were not computed."
        ),
    },
    "yt-3d": {
        "title": "YouTube public search: beginner 3D printing",
        "url": "https://www.youtube.com/results?search_query=3D+printer+beginner",
        "retrieved": RETRIEVED,
        "kind": "public-search-snapshot",
        "detail": (
            "CNC Kitchen's beginner guide showed 628,777 views at 9 months. "
            "3D Print Dood's 2026 beginner guide showed 36,910 views at 3 weeks."
        ),
    },
}

COMPETITORS = {
    "damien": {"name": "Damien Talks Money", "handle": "@DamienTalksMoney", "market": "UK", "subs_label": "420k", "evidence": "yt-damien"},
    "james": {"name": "James Shack", "handle": "@JamesShack", "market": "UK", "subs_label": "283k", "evidence": "yt-james"},
    "pensioncraft": {"name": "PensionCraft", "handle": "@Pensioncraft", "market": "UK", "subs_label": "219k", "evidence": "yt-pensioncraft"},
    "toby": {"name": "Toby Newbatt", "handle": "@TobyNewbatt", "market": "UK", "subs_label": "203k", "evidence": "yt-toby"},
    "nischa": {"name": "Nischa", "handle": "@nischa", "market": "UK", "subs_label": "2.27m", "evidence": "yt-nischa"},
    "beclever": {"name": "Be Clever With Your Cash", "handle": "@BeCleverWithYourCash", "market": "UK", "subs_label": "120k", "evidence": "yt-beclever"},
    "humphrey": {"name": "Humphrey Yang", "handle": "@humphrey", "market": "US", "subs_label": "2.09m", "evidence": "yt-humphrey"},
    "tina": {"name": "Tina Huang", "handle": "@TinaHuang1", "market": "US", "subs_label": "1.36m", "evidence": "yt-tina"},
    "matt": {"name": "Matt Wolfe", "handle": "@mreflow", "market": "US", "subs_label": "1.02m", "evidence": "yt-matt"},
    "leila": {"name": "Leila Gharani", "handle": "@LeilaGharani", "market": "US", "subs_label": "3.09m", "evidence": "yt-leila"},
    "medicare": {"name": "Medicare School", "handle": "@MedicareSchool", "market": "US", "subs_label": "375k", "evidence": "yt-medicare"},
    "ken": {"name": "Ken McElroy", "handle": "@KenMcElroy", "market": "US", "subs_label": "528k", "evidence": "yt-ken"},
    "sorted": {"name": "Sorted Food", "handle": "@SortedFood", "market": "UK", "subs_label": "3.01m", "evidence": "yt-sorted"},
}

DNA = {
    "uk_investing": {
        "observed": (
            "Outlier public videos in this cluster run 15–23 minutes and put a concrete "
            "UK number in the premise: a salary, a house-price question, an ISA allowance, "
            "or a portfolio size. Damien's house video (1.05 million views in three weeks "
            "on a 420k-subscriber channel) and salary video (377,936 views in eight days) "
            "both outran the subscriber label. PensionCraft's calmer £10k/£100k/£1m video "
            "was 47,818 views in seven days on 219k subscribers, so the same topic does "
            "not automatically travel."
        ),
        "principle": (
            "Use one decision and one official figure, then show the arithmetic. Close "
            "the question the title opens. Keep episodes materially different: a salary "
            "band is not a house-price episode and is not an ISA-rule episode."
        ),
        "not_observed": "Frames, thumbnails, music, voice timbre, and retention curves were not captured. No competitor script, shot list, or title is reused.",
    },
    "uk_retirement": {
        "observed": (
            "James Shack, 283k subscribers: 2,072,923 views in one month on a 14:59 video, "
            "831,417 views in three weeks on a 19:07 video, and 313,658 views in two months "
            "on an 18:23 spending video. The public pattern is a single retirement question "
            "with pounds and ages, in a quarter-hour to twenty minutes."
        ),
        "principle": "Show the assumption table before the result. A rate from a title is not a quote. Each episode changes the question, the pot size, or the income type.",
        "not_observed": "Frame timing, camera moves, and audio mix were not measured.",
    },
    "uk_cash": {
        "observed": "Be Clever With Your Cash, 120k subscribers, recent 13–18 minute explainers between about 5k and 44k views. Demand is visible and modest.",
        "principle": "Name the product mechanic, the date of the rate, and the penalty. Do not present a rate as permanent.",
        "not_observed": "Thumbnail tests and retention were not available.",
    },
    "us_milestones": {
        "observed": (
            "Humphrey Yang, 2.09m subscribers, posted four 15–17 minute videos in four weeks. "
            "The largest, a $0-to-$1M milestone video, had 961,448 views at four weeks, "
            "under half the subscriber label. Cadence is steadier than breakout."
        ),
        "principle": "Change the dollar threshold every episode and show the formula. A milestone series is allowed when the numbers and the lesson change.",
        "not_observed": "Opening-frame duration and music were not measured.",
    },
    "ai_screen": {
        "observed": (
            "Tina Huang, 1.36m subscribers: 1,753,336 views in three weeks on a 24-minute "
            "local-model explainer, and 256,498 views in four days on a 25-minute roadmap. "
            "Matt Wolfe, 1.02m subscribers, holds a weekly 26–31 minute briefing at "
            "75k–177k views inside a week."
        ),
        "principle": (
            "Record the screen, start from a real task, and keep a human judgment in the "
            "edit. AI is the tool under test, never the expert on camera. A news briefing "
            "and a single-task test are different series."
        ),
        "not_observed": "Scene cuts and b-roll were not frame-measured.",
    },
    "excel": {
        "observed": (
            "Leila Gharani, 3.09m subscribers: a 10:31 technique video had 321,927 views "
            "at one month. Lifetime beginner courses on Kevin Stratvert's catalog still "
            "show millions of views years later. Recent views per subscriber are modest."
        ),
        "principle": "One operation, one workbook, one before-and-after. Screen recording carries the episode.",
        "not_observed": "Mouse-path pacing was not measured.",
    },
    "medicare": {
        "observed": (
            "Medicare School, 375k subscribers. The stronger public video in the snapshot "
            "had 335,240 views at six months. That is a catalog, not a 30-day spike."
        ),
        "principle": "Read the Medicare.gov chart on screen. Compare plan letters. Give no personal recommendation and use no synthetic clinician.",
        "not_observed": "Thumbnail layout and narration pace were not measured.",
    },
    "property": {
        "observed": "Ken McElroy, 528k subscribers: 72,687 views in two weeks on a 16-minute market video. Modest relative to the subscriber label.",
        "principle": "Teach a document (offer, inspection, closing disclosure, stamp duty) rather than a price prediction.",
        "not_observed": "Graphics style was not captured.",
    },
    "food": {
        "observed": "Sorted Food, 3.01m subscribers, draws several hundred thousand views in days on cast challenge episodes of 17–24 minutes.",
        "principle": "Cook an original recipe with weights and a technique. Do not restage their challenges, cast, or sabotage format.",
        "not_observed": "Edit rhythm inside those episodes was not frame-measured.",
    },
    "hobby": {
        "observed": "MJ Aquascaping, 270k subscribers, 38k–70k views across two weeks. Keyboard videos showed mid-six-figure views over several months without a subscriber denominator.",
        "principle": "One build step or one buying term per episode. Film the work.",
        "not_observed": "Color grade and music beds were not sampled.",
    },
    "senior": {
        "observed": "First-page long tutorials were often under 10k views, with one older iPhone basics video at 294,366 views after two years.",
        "principle": "One setting, large type, a full click path, and a warning about fake login pages. Pace for a first-time user.",
        "not_observed": "Whether those low counts mean low demand or weak videos cannot be separated without search-volume data.",
    },
    "homeschool": {
        "observed": "Recent parent-curriculum videos on the first page were about 6k–33k views.",
        "principle": "Talk to parents about planning and records. The channel is not made for children.",
        "not_observed": "Retention and search volume were not measured.",
    },
    "general_gap": {
        "observed": "No fresh view-per-subscriber pair was captured for this sub-niche on 24 October 2026.",
        "principle": "Hold the editorial angle until a public search snapshot shows a repeatable long-form pattern. Do not backfill fake velocity.",
        "not_observed": "7, 30, and 90 day analytics were not available.",
    },
}

# id, name, handle, market, category, niche, audience, monetization, velocity,
# competition, policy, dna, duration, days, hour_local, tz, evidence, competitors, launch
RAW = [
    ("uk-salary-ledger", "Salary Ledger", "salaryledger", "UK", "Personal finance education", "How a UK investing setup changes across salary bands", "UK employees, 22–45, with a workplace pension and no stocks-and-shares ISA yet", "finance", "breakout", "workable", "sourced", "uk_investing", "16–22 min", "Tue,Thu,Sat,Sun", "18:10", "Europe/London", ["yt-damien", "govuk-isa", "ii-gbrs", "ypp-inauthentic", "air-rpm"], ["damien", "toby", "nischa"], True),
    ("uk-drawdown-desk", "Drawdown Desk", "drawdowndesk", "UK", "Retirement education", "Retirement spending math with the assumptions written down", "UK households within ten years of drawing a pension", "finance", "breakout", "workable", "sourced", "uk_retirement", "15–20 min", "Mon,Wed,Fri,Sun", "11:20", "Europe/London", ["yt-james", "yt-pensioncraft", "ii-gbrs", "ypp-inauthentic", "air-rpm"], ["james", "pensioncraft"], True),
    ("uk-allowance-note", "Allowance Note", "allowancenote", "UK", "Tax-wrapper education", "ISA rules for the 2026/27 year and the April 2027 cash change", "UK adults deciding where the annual allowance goes", "finance", "strong", "workable", "sourced", "uk_investing", "12–16 min", "Tue,Thu,Sat,Sun", "12:40", "Europe/London", ["govuk-isa", "yt-toby", "yt-damien", "ypp-inauthentic"], ["toby", "damien"], False),
    ("uk-pension-plain", "Pension Plain", "pensionplain", "UK", "Workplace pension education", "What employee and employer contributions do inside a workplace pension", "People auto-enrolled in a UK workplace scheme", "finance", "strong", "workable", "sourced", "uk_investing", "14–18 min", "Mon,Wed,Fri,Sun", "19:05", "Europe/London", ["yt-damien", "ii-gbrs", "ypp-inauthentic", "air-rpm"], ["damien", "pensioncraft"], False),
    ("uk-remortgage-hour", "Remortgage Hour", "remortgagehour", "UK", "Mortgage education", "How a UK remortgage quote is built, without a rate prediction", "Homeowners coming to the end of a fixed rate", "finance", "strong", "workable", "sourced", "uk_investing", "14–18 min", "Tue,Thu,Sat,Sun", "07:30", "Europe/London", ["yt-toby", "yt-damien", "ypp-inauthentic"], ["toby", "damien"], False),
    ("uk-cash-ladder", "Cash Ladder", "cashladderuk", "UK", "Cash savings education", "Emergency funds and the difference between easy-access and fixed savings", "UK savers comparing cash products", "finance", "modest", "workable", "sourced", "uk_cash", "12–16 min", "Mon,Wed,Fri,Sun", "08:15", "Europe/London", ["yt-beclever", "ypp-inauthentic", "air-rpm"], ["beclever"], False),
    ("uk-return-desk", "Return Desk", "returndesk", "UK", "Self Assessment education", "Screen walkthrough of public HMRC Self Assessment guidance for a sole trader", "First-time Self Assessment filers", "finance", "modest", "open", "tutorial", "general_gap", "18–24 min", "Tue,Thu,Sat,Sun", "20:10", "Europe/London", ["ypp-inauthentic", "air-rpm", "vidiq-niches"], [], False),
    ("uk-forecast-line", "Forecast Line", "forecastline", "UK", "State Pension education", "How to read a State Pension forecast and what it does not promise", "UK adults checking a State Pension forecast", "finance", "modest", "workable", "sourced", "uk_retirement", "12–16 min", "Mon,Wed,Fri,Sun", "13:30", "Europe/London", ["yt-james", "ii-gbrs", "ypp-inauthentic"], ["james"], False),
    ("uk-first-key", "First Key", "firstkeyuk", "UK", "First-time buyer education", "The England and Wales purchase sequence from agreement in principle to completion", "Renters planning a first purchase", "finance", "modest", "workable", "sourced", "property", "16–20 min", "Tue,Thu,Sat,Sun", "17:40", "Europe/London", ["yt-damien", "yt-ken", "ypp-inauthentic"], ["damien"], False),
    ("uk-rent-record", "Rent Record", "rentrecorduk", "UK", "Landlord record-keeping", "Records a small UK landlord keeps for property income", "Accidental landlords with one property", "finance", "unknown", "workable", "sourced", "property", "14–18 min", "Mon,Wed,Fri,Sun", "18:45", "Europe/London", ["yt-ken", "ypp-inauthentic", "air-rpm"], ["ken"], False),
    ("uk-maintenance-loan", "Maintenance Note", "maintenancenote", "UK", "Student finance education", "How UK student maintenance loans are described in public guidance, for parents", "Parents of students, adult audience", "finance", "unknown", "open", "sourced", "general_gap", "12–16 min", "Tue,Thu,Sat,Sun", "09:20", "Europe/London", ["vidiq-niches", "ypp-inauthentic"], [], False),
    ("uk-independence-math", "Independence Math", "independencemath", "UK", "Financial independence education", "Savings-rate arithmetic with every assumption labeled", "UK professionals curious about leaving work earlier", "finance", "unknown", "crowded", "sourced", "uk_retirement", "16–20 min", "Mon,Wed,Fri,Sun", "20:40", "Europe/London", ["yt-james", "ii-gbrs", "ypp-inauthentic"], ["james", "nischa"], False),
    ("us-mile-marker", "Mile Marker", "milemarkerus", "US", "Personal finance education", "What the math changes at successive net-worth thresholds", "US wage earners tracking a net-worth number", "finance", "steady", "crowded", "sourced", "us_milestones", "15–18 min", "Mon,Wed,Fri,Sun", "12:10", "America/New_York", ["yt-humphrey", "air-rpm", "ypp-inauthentic"], ["humphrey"], False),
    ("us-index-plain", "Index Plain", "indexplain", "US", "Index-fund education", "How a market-cap index fund is built and what it does not guarantee", "New US brokerage users", "finance", "steady", "crowded", "sourced", "us_milestones", "14–18 min", "Tue,Thu,Sat,Sun", "16:30", "America/New_York", ["yt-humphrey", "air-rpm", "ypp-inauthentic", "vidiq-niches"], ["humphrey"], False),
    ("us-paycheck-split", "Paycheck Split", "paychecksplit", "US", "Budgeting education", "Three budgeting methods compared as methods, with a worked paycheck", "US households living on a salary", "finance", "unknown", "crowded", "sourced", "general_gap", "13–17 min", "Mon,Wed,Fri,Sun", "07:10", "America/Chicago", ["air-rpm", "vidiq-niches", "ypp-inauthentic"], [], False),
    ("us-credit-mechanics", "Credit Mechanics", "creditmechanics", "US", "Consumer-credit education", "Statement balances, utilization, and interest as mechanics", "US adults with a first credit card", "finance", "unknown", "crowded", "sourced", "general_gap", "12–16 min", "Tue,Thu,Sat,Sun", "19:15", "America/New_York", ["air-rpm", "ypp-inauthentic"], [], False),
    ("us-tax-year-desk", "Tax Year Desk", "taxyeardesk", "US", "Individual tax education", "W-2 concepts from IRS publications, screen-recorded", "Employees filing a simple return", "finance", "unknown", "crowded", "tutorial", "excel", "16–22 min", "Mon,Wed,Fri,Sun", "11:00", "America/New_York", ["air-rpm", "ypp-inauthentic"], [], False),
    ("us-roth-versus", "Roth Versus", "rothversus", "US", "Retirement-account education", "Traditional and Roth definitions, contribution concepts, and the questions a form asks", "US workers choosing a workplace plan", "finance", "unknown", "crowded", "sourced", "general_gap", "14–18 min", "Tue,Thu,Sat,Sun", "13:45", "America/Chicago", ["yt-humphrey", "ypp-inauthentic", "air-rpm"], ["humphrey"], False),
    ("us-hsa-desk", "HSA Desk", "hsadesk", "US", "Health-savings education", "What an HSA form is for, and what it is not", "US workers offered a high-deductible plan", "finance", "unknown", "workable", "sourced", "general_gap", "12–16 min", "Mon,Wed,Fri,Sun", "18:20", "America/New_York", ["ypp-inauthentic", "air-rpm"], [], False),
    ("us-estate-paper", "Estate Paper", "estatepaper", "US", "Estate-document education", "Why a will is a state-specific document, and where a state-bar referral list lives", "Adults who have never written a will", "finance", "unknown", "workable", "sourced", "general_gap", "12–15 min", "Tue,Thu,Sat,Sun", "08:40", "America/New_York", ["ypp-inauthentic"], [], False),
    ("us-debt-order", "Debt Order", "debtorder", "US", "Debt-payoff education", "Avalanche and snowball as arithmetic, on the same fictional balances", "People comparing two payoff sequences", "finance", "unknown", "crowded", "sourced", "general_gap", "12–16 min", "Mon,Wed,Fri,Sun", "20:05", "America/Chicago", ["air-rpm", "ypp-inauthentic"], [], False),
    ("us-one-fund", "One Fund Question", "onefundquestion", "US", "Fund-structure education", "What a single global equity fund contains and what it leaves out", "Beginners asking if one fund is enough", "finance", "steady", "crowded", "sourced", "us_milestones", "14–18 min", "Tue,Thu,Sat,Sun", "15:10", "America/New_York", ["yt-humphrey", "ypp-inauthentic"], ["humphrey"], False),
    ("us-coverage-map", "Coverage Map", "coveragemap", "US", "Medicare education", "Original Medicare, Medicare Advantage, and Medigap as three different structures", "Adults approaching Medicare enrollment", "unverified", "modest", "workable", "sourced", "medicare", "16–22 min", "Mon,Wed,Fri,Sun", "10:30", "America/New_York", ["yt-medicare", "medicare-compare", "ypp-inauthentic"], ["medicare"], True),
    ("us-letter-plans", "Letter Plans", "letterplans", "US", "Medigap education", "How to read the Medicare.gov letter chart without picking a policy for someone", "People comparing Medigap letters", "unverified", "modest", "workable", "sourced", "medicare", "14–18 min", "Tue,Thu,Sat,Sun", "14:20", "America/Chicago", ["medicare-compare", "yt-medicare", "ypp-inauthentic"], ["medicare"], False),
    ("us-enrollment-window", "Enrollment Window", "enrollmentwindow", "US", "Medicare timing education", "The names of the public enrollment windows and what each one is for", "People unsure which Medicare deadline applies", "unverified", "modest", "workable", "sourced", "medicare", "12–16 min", "Mon,Wed,Fri,Sun", "09:00", "America/New_York", ["medicare-compare", "yt-medicare", "ypp-inauthentic"], ["medicare"], False),
    ("us-bench-test", "Bench Test", "benchtestai", "US", "AI workflow education", "A repeatable way to test one AI tool on one real task", "Professionals who need a method, not a model roundup", "education", "strong", "crowded", "tutorial", "ai_screen", "14–20 min", "Tue,Thu,Sat,Sun", "11:40", "America/New_York", ["yt-tina", "yt-matt", "ypp-inauthentic", "air-rpm", "vidiq-niches"], ["tina", "matt"], True),
    ("us-brief-safe", "Brief Safe", "briefsafe", "US", "AI writing education", "How to test a writing tool without pasting client secrets", "Freelancers and agency staff", "education", "steady", "crowded", "tutorial", "ai_screen", "12–16 min", "Mon,Wed,Fri,Sun", "15:50", "America/New_York", ["yt-matt", "yt-tina", "ypp-inauthentic"], ["matt", "tina"], False),
    ("us-sheet-shift", "Sheet Shift", "sheetshift", "US", "Spreadsheet education", "Moving a repeated Excel copy-paste into one query or formula", "Operators who live in workbooks", "education", "modest", "giant", "tutorial", "excel", "10–16 min", "Tue,Thu,Sat,Sun", "09:35", "America/Chicago", ["yt-leila", "air-rpm", "ypp-inauthentic"], ["leila"], False),
    ("us-inbox-triage", "Inbox Triage", "inboxtriage", "US", "Workplace AI education", "A review step for AI-drafted email before it is sent", "People who answer a high volume of email", "education", "steady", "crowded", "tutorial", "ai_screen", "10–14 min", "Mon,Wed,Fri,Sun", "08:25", "America/New_York", ["yt-matt", "ypp-inauthentic"], ["matt"], False),
    ("us-lesson-bench", "Lesson Bench", "lessonbench", "US", "Teacher-tool education", "Using an AI draft for a lesson plan that a teacher still edits", "Classroom teachers, adult audience", "education", "steady", "workable", "tutorial", "ai_screen", "12–16 min", "Tue,Thu,Sat,Sun", "16:00", "America/Chicago", ["yt-tina", "vidiq-niches", "ypp-inauthentic"], ["tina"], False),
    ("us-listing-desk", "Listing Desk", "listingdesk", "US", "Real-estate writing education", "Drafting a listing description and checking it against fair-housing language", "Agents who write listings", "education", "unknown", "workable", "tutorial", "ai_screen", "12–16 min", "Mon,Wed,Fri,Sun", "13:15", "America/New_York", ["vidiq-niches", "ypp-inauthentic"], [], False),
    ("us-clinic-admin", "Clinic Admin", "clinicadmin", "US", "Office-workflow education", "Appointment-reminder templates that do not give medical advice", "Clinic coordinators", "education", "unknown", "open", "tutorial", "general_gap", "10–14 min", "Tue,Thu,Sat,Sun", "07:50", "America/Chicago", ["vidiq-niches", "ypp-inauthentic"], [], False),
    ("us-research-notebook", "Research Notebook", "researchnotebook", "US", "Study-skills education", "How to keep a citation when a study tool helps with a reading", "University students and researchers", "education", "steady", "crowded", "tutorial", "ai_screen", "12–16 min", "Mon,Wed,Fri,Sun", "17:25", "America/New_York", ["yt-tina", "air-rpm"], ["tina"], False),
    ("us-diff-desk", "Diff Desk", "diffdesk", "US", "Programming-assistant education", "Reviewing an AI code suggestion on a small original example", "Working developers", "education", "strong", "crowded", "tutorial", "ai_screen", "14–20 min", "Tue,Thu,Sat,Sun", "18:30", "America/New_York", ["yt-tina", "yt-matt", "ypp-inauthentic"], ["tina", "matt"], False),
    ("us-support-macros", "Support Macros", "supportmacros", "US", "Support-writing education", "A QA checklist for AI-drafted customer replies", "Support leads", "education", "steady", "workable", "tutorial", "ai_screen", "10–14 min", "Mon,Wed,Fri,Sun", "12:55", "America/Chicago", ["yt-matt", "ypp-inauthentic"], ["matt"], False),
    ("us-pivot-shop", "Pivot Shop", "pivotshop", "US", "Excel education", "Pivot tables for a simple inventory", "Small-team operators", "education", "modest", "giant", "tutorial", "excel", "12–18 min", "Tue,Thu,Sat,Sun", "10:15", "America/New_York", ["yt-leila", "air-rpm"], ["leila"], False),
    ("us-query-bench", "Query Bench", "querybench", "US", "Power Query education", "Appending monthly files without copy-paste", "Analysts who receive monthly workbooks", "education", "modest", "giant", "tutorial", "excel", "14–20 min", "Mon,Wed,Fri,Sun", "19:40", "America/New_York", ["yt-leila", "ypp-inauthentic"], ["leila"], False),
    ("uk-one-page-plan", "One Page Plan", "onepageplan", "UK", "Project-management education", "A one-page plan: outcome, date, owner, risk", "New project leads", "education", "unknown", "workable", "tutorial", "general_gap", "10–14 min", "Tue,Thu,Sat,Sun", "13:00", "Europe/London", ["vidiq-niches", "air-rpm"], [], False),
    ("uk-decision-log", "Decision Log", "decisionlog", "UK", "Meeting education", "Writing a decision so the meeting can end", "Team leads", "education", "unknown", "open", "tutorial", "general_gap", "8–12 min", "Mon,Wed,Fri,Sun", "08:55", "Europe/London", ["vidiq-niches"], [], False),
    ("uk-sop-studio", "SOP Studio", "sopstudio", "UK", "Operations writing", "A standard operating procedure with a test step", "Owners documenting a five-person team", "education", "unknown", "open", "tutorial", "general_gap", "12–16 min", "Tue,Thu,Sat,Sun", "15:35", "Europe/London", ["vidiq-niches"], [], False),
    ("uk-invoice-desk", "Invoice Desk", "invoicedesk", "UK", "Small-business admin", "The fields an invoice needs and how to chase one", "Freelancers sending a first invoice", "education", "unknown", "workable", "tutorial", "general_gap", "10–14 min", "Mon,Wed,Fri,Sun", "16:45", "Europe/London", ["vidiq-niches", "air-rpm"], [], False),
    ("us-book-square", "Book Square", "booksquare", "US", "Bookkeeping education", "A chart of accounts for a one-product service business", "Owners doing their own books", "education", "modest", "workable", "tutorial", "excel", "16–22 min", "Tue,Thu,Sat,Sun", "18:05", "America/Chicago", ["yt-leila", "air-rpm", "ypp-inauthentic"], ["leila"], False),
    ("us-first-hire", "First Hire", "firsthireus", "US", "Payroll-concept education", "The public forms a first US hire tends to involve, read from agency pages", "Owners hiring employee number one", "education", "unknown", "workable", "tutorial", "general_gap", "14–18 min", "Mon,Wed,Fri,Sun", "11:35", "America/New_York", ["ypp-inauthentic", "air-rpm"], [], False),
    ("us-offer-paper", "Offer Paper", "offerpaper", "US", "Home-purchase education", "The parts of a US purchase offer", "First-time buyers before they write an offer", "unverified", "modest", "workable", "sourced", "property", "14–18 min", "Tue,Thu,Sat,Sun", "12:25", "America/New_York", ["yt-ken", "ypp-inauthentic"], ["ken"], False),
    ("us-inspection-list", "Inspection List", "inspectionlist", "US", "Home-inspection education", "How to read sections of an inspection report", "Buyers who just received a report", "unverified", "modest", "workable", "sourced", "property", "14–18 min", "Mon,Wed,Fri,Sun", "17:50", "America/Chicago", ["yt-ken", "ypp-inauthentic"], ["ken"], False),
    ("us-rent-roll", "Rent Roll", "rentrollus", "US", "Small-landlord education", "How to read a one-page rent roll", "Buyers of a small rental", "finance", "modest", "workable", "sourced", "property", "12–16 min", "Tue,Thu,Sat,Sun", "19:55", "America/New_York", ["yt-ken", "air-rpm"], ["ken"], False),
    ("us-rate-lock", "Rate Lock", "ratelock", "US", "Mortgage-process education", "What a rate lock is and what it does not freeze", "Borrowers with a live application", "finance", "unknown", "workable", "sourced", "property", "10–14 min", "Mon,Wed,Fri,Sun", "07:40", "America/New_York", ["yt-ken", "ypp-inauthentic"], ["ken"], False),
    ("us-closing-table", "Closing Table", "closingtable", "US", "Closing-disclosure education", "A walkthrough of the sections on a closing disclosure", "Buyers a week from closing", "finance", "unknown", "workable", "sourced", "property", "16–20 min", "Tue,Thu,Sat,Sun", "10:45", "America/Chicago", ["ypp-inauthentic", "air-rpm"], [], False),
    ("uk-stamp-desk", "Stamp Desk", "stampdesk", "UK", "Stamp Duty education", "How to find the public Stamp Duty rules for a purchase", "England and Northern Ireland buyers", "finance", "unknown", "workable", "sourced", "property", "12–16 min", "Mon,Wed,Fri,Sun", "12:15", "Europe/London", ["yt-toby", "ypp-inauthentic"], ["toby"], False),
    ("uk-survey-types", "Survey Types", "surveytypes", "UK", "Home-survey education", "The difference between common UK home-survey levels", "Buyers choosing a survey", "unverified", "unknown", "open", "sourced", "property", "12–15 min", "Tue,Thu,Sat,Sun", "14:05", "Europe/London", ["vidiq-niches", "ypp-inauthentic"], [], False),
    ("uk-service-charge", "Service Charge", "servicechargeuk", "UK", "Leasehold education", "How to read a service-charge demand", "Leasehold flat owners", "finance", "unknown", "open", "sourced", "property", "12–16 min", "Mon,Wed,Fri,Sun", "16:20", "Europe/London", ["ypp-inauthentic", "air-rpm"], [], False),
    ("uk-weeknight-gram", "Weeknight Gram", "weeknightgram", "UK", "Home cooking", "Original 30-minute UK recipes with gram weights", "People cooking after work", "food", "unknown", "giant", "food", "food", "12–18 min", "Tue,Thu,Sat,Sun", "17:15", "Europe/London", ["yt-sorted", "air-rpm"], ["sorted"], False),
    ("uk-one-tin", "One Tin", "onetinuk", "UK", "Pantry cooking", "Original meals that start from tinned ingredients", "Budget home cooks", "food", "unknown", "giant", "food", "food", "10–15 min", "Mon,Wed,Fri,Sun", "18:00", "Europe/London", ["yt-sorted", "air-rpm"], ["sorted"], False),
    ("us-sunday-batch", "Sunday Batch", "sundaybatch", "US", "Meal prep", "Component prep for five different plates, original recipes", "People who cook once on Sunday", "food", "unknown", "giant", "food", "food", "14–20 min", "Tue,Thu,Sat,Sun", "11:10", "America/Chicago", ["air-rpm", "vidiq-niches"], [], False),
    ("uk-heat-control", "Heat Control", "heatcontrol", "UK", "Cooking technique", "Sear, simmer, and residual heat as separate skills", "Home cooks past beginner recipes", "food", "unknown", "giant", "food", "food", "8–12 min", "Mon,Wed,Fri,Sun", "17:05", "Europe/London", ["air-rpm"], [], False),
    ("us-grocery-math", "Grocery Math", "grocerymath", "US", "Food shopping literacy", "Unit price, package size, and a worked basket", "Households comparing supermarket prices", "food", "unknown", "crowded", "food", "food", "8–12 min", "Tue,Thu,Sat,Sun", "08:05", "America/Chicago", ["air-rpm", "vidiq-niches"], [], False),
    ("uk-bread-window", "Bread Window", "breadwindow", "UK", "Home bread", "An original timetable for one loaf, from mix to cool", "Weekend bakers", "food", "unknown", "crowded", "food", "food", "14–20 min", "Mon,Wed,Fri,Sun", "09:45", "Europe/London", ["air-rpm"], [], False),
    ("uk-knife-basics", "Knife Basics", "knifebasics", "UK", "Kitchen skill", "Grip, claw, and three cuts, filmed on a board", "New home cooks", "food", "unknown", "giant", "food", "food", "8–12 min", "Tue,Thu,Sat,Sun", "12:50", "Europe/London", ["vidiq-niches"], [], False),
    ("uk-packed-desk", "Packed Desk", "packeddesk", "UK", "Adult packed meals", "Original packed lunches for office days", "Adults packing their own lunch", "food", "unknown", "crowded", "food", "food", "8–12 min", "Mon,Wed,Fri,Sun", "07:20", "Europe/London", ["yt-sorted", "air-rpm"], ["sorted"], False),
    ("us-rep-notes", "Rep Notes", "repnotes", "US", "Strength training", "How to log sets so the next session has a target", "People following a simple barbell plan", "fitness", "unknown", "giant", "fitness", "general_gap", "10–14 min", "Tue,Thu,Sat,Sun", "06:40", "America/New_York", ["vidiq-niches", "air-rpm"], [], False),
    ("uk-band-setup", "Band Setup", "bandsetup", "UK", "Resistance-band training", "Anchor, line of pull, and three patterns", "Home trainees with a band and a door anchor", "fitness", "unknown", "crowded", "fitness", "general_gap", "10–14 min", "Mon,Wed,Fri,Sun", "06:10", "Europe/London", ["vidiq-niches"], [], False),
    ("uk-desk-mobility", "Desk Mobility", "deskmobility", "UK", "Mobility", "A short routine for people who sit at a desk", "Office workers", "fitness", "unknown", "crowded", "fitness", "general_gap", "8–12 min", "Tue,Thu,Sat,Sun", "12:05", "Europe/London", ["vidiq-niches"], [], False),
    ("us-run-easy", "Run Easy", "runeasy", "US", "Running education", "Easy pace as a conversation test, not a medical plan", "New runners", "fitness", "unknown", "giant", "fitness", "general_gap", "10–14 min", "Mon,Wed,Fri,Sun", "06:55", "America/New_York", ["vidiq-niches"], [], False),
    ("us-label-read", "Label Read", "labelread", "US", "Food-label literacy", "Protein, serving size, and the difference between a label and a diet", "Shoppers reading the back of a tub", "fitness", "unknown", "crowded", "fitness", "general_gap", "8–12 min", "Tue,Thu,Sat,Sun", "17:55", "America/Chicago", ["air-rpm"], [], False),
    ("uk-warmup-ten", "Warmup Ten", "warmupten", "UK", "General warmup", "Ten minutes of general movement before a workout", "Gym beginners", "fitness", "unknown", "giant", "fitness", "general_gap", "10–12 min", "Mon,Wed,Fri,Sun", "15:25", "Europe/London", ["vidiq-niches"], [], False),
    ("us-keystroke", "Keystroke", "keystroke", "US", "Keyboard buying education", "Switches, profiles, and what a spec sheet actually says", "People buying a first mechanical keyboard", "hobby", "unknown", "workable", "hobby", "hobby", "12–18 min", "Tue,Thu,Sat,Sun", "20:20", "America/New_York", ["yt-keys", "vidiq-niches"], [], False),
    ("us-first-layer", "First Layer", "firstlayer", "US", "3D-printing education", "First-layer height, temperature, and a failed print you can see", "Owners of a first printer", "hobby", "modest", "workable", "hobby", "hobby", "14–20 min", "Mon,Wed,Fri,Sun", "19:10", "America/Chicago", ["yt-3d", "vidiq-niches"], [], False),
    ("uk-brew-ratio", "Brew Ratio", "brewratio", "UK", "Home coffee", "One brewer, three ratios, a repeatable tasting note", "Home brewers", "hobby", "unknown", "crowded", "hobby", "hobby", "10–14 min", "Tue,Thu,Sat,Sun", "08:50", "Europe/London", ["vidiq-niches"], [], False),
    ("us-hardscape", "Hardscape", "hardscape", "US", "Aquascaping", "Rock placement and a planting order for a new tank", "Freshwater hobbyists", "hobby", "modest", "workable", "hobby", "hobby", "14–22 min", "Mon,Wed,Fri,Sun", "14:40", "America/New_York", ["yt-aqua", "vidiq-niches"], [], False),
    ("uk-spine-sew", "Spine Sew", "spinesew", "UK", "Bookbinding", "One stitch and one pamphlet, start to finish", "Craft beginners", "craft", "unknown", "open", "craft", "hobby", "12–18 min", "Tue,Thu,Sat,Sun", "15:15", "Europe/London", ["vidiq-niches", "air-rpm"], [], False),
    ("uk-line-walk", "Line Walk", "linewalk", "UK", "Urban sketching", "A 20-minute sketch exercise in a public place", "People learning to draw on location", "craft", "unknown", "open", "craft", "hobby", "8–14 min", "Mon,Wed,Fri,Sun", "10:20", "Europe/London", ["vidiq-niches"], [], False),
    ("us-call-the-pro", "Call the Pro", "callthepro", "US", "Home-safety education", "Jobs that belong to a licensed electrician, and the signs to stop", "Homeowners tempted by a panel video", "unverified", "unknown", "open", "sourced", "general_gap", "8–12 min", "Tue,Thu,Sat,Sun", "18:40", "America/Chicago", ["ypp-inauthentic"], [], False),
    ("us-filter-month", "Filter Month", "filtermonth", "US", "Home maintenance", "Replacing a standard HVAC filter and when to stop", "Renters and owners", "unverified", "unknown", "open", "hobby", "general_gap", "6–10 min", "Mon,Wed,Fri,Sun", "09:30", "America/New_York", ["vidiq-niches"], [], False),
    ("us-larger-type", "Larger Type", "largertype", "US", "Senior digital skills", "Making phone text larger, one settings path", "Adults teaching a parent, and older adults", "unverified", "modest", "open", "tutorial", "senior", "8–12 min", "Tue,Thu,Sat,Sun", "10:00", "America/New_York", ["yt-senior", "vidiq-niches", "ypp-inauthentic"], [], False),
    ("us-bank-check", "Bank Check", "bankcheck", "US", "Phishing awareness", "How a real bank login looks, and what a fake page asks for", "Older adults who bank on a phone", "unverified", "modest", "open", "tutorial", "senior", "10–14 min", "Mon,Wed,Fri,Sun", "11:15", "America/Chicago", ["yt-senior", "vidiq-niches"], [], False),
    ("us-photo-send", "Photo Send", "photosend", "US", "Smartphone basics", "Sending one photo to one contact, slowly", "First-time smartphone users", "unverified", "modest", "open", "tutorial", "senior", "8–12 min", "Tue,Thu,Sat,Sun", "14:55", "America/New_York", ["yt-senior", "vidiq-niches"], [], False),
    ("us-appointment-tap", "Appointment Tap", "appointmenttap", "US", "Calendar basics", "Putting a doctor appointment on a phone calendar", "People who still use a paper diary", "unverified", "modest", "open", "tutorial", "senior", "8–12 min", "Mon,Wed,Fri,Sun", "13:40", "America/Chicago", ["yt-senior", "vidiq-niches"], [], False),
    ("us-charge-curve", "Charge Curve", "chargecurve", "US", "EV education", "What a charging-speed claim means on a spec sheet", "First-time EV buyers", "transport", "unknown", "crowded", "sourced", "general_gap", "12–16 min", "Tue,Thu,Sat,Sun", "16:15", "America/New_York", ["air-rpm", "vidiq-niches"], [], False),
    ("us-home-plug", "Home Plug", "homeplug", "US", "EV charging education", "Questions to take to an electrician before a home charger", "Homeowners considering a charger", "transport", "unknown", "workable", "sourced", "general_gap", "10–14 min", "Mon,Wed,Fri,Sun", "18:35", "America/Chicago", ["air-rpm"], [], False),
    ("us-used-pack", "Used Pack", "usedpack", "US", "Used-EV education", "Warranty questions to ask about a used traction battery", "Used-EV shoppers", "transport", "unknown", "crowded", "sourced", "general_gap", "12–16 min", "Tue,Thu,Sat,Sun", "09:05", "America/New_York", ["air-rpm", "vidiq-niches"], [], False),
    ("uk-phrase-workshop", "Phrase Workshop", "phraseworkshop", "UK", "English lessons", "Original intermediate phrases, taught and then used in a scene", "Adult English learners", "education", "unknown", "crowded", "tutorial", "general_gap", "10–14 min", "Mon,Wed,Fri,Sun", "20:30", "Europe/London", ["vidiq-niches", "air-rpm", "ypp-inauthentic"], [], False),
    ("us-work-english", "Work English", "workenglish", "US", "Workplace English", "Phrases for a status update, a delay, and a request", "Adults working in English as an additional language", "education", "unknown", "workable", "tutorial", "general_gap", "8–12 min", "Tue,Thu,Sat,Sun", "07:15", "America/Chicago", ["vidiq-niches", "air-rpm"], [], False),
    ("uk-kitchen-english", "Kitchen English", "kitchenenglish", "UK", "Vocabulary", "Cooking verbs, demonstrated, then reused", "Adult learners who cook", "education", "unknown", "workable", "tutorial", "general_gap", "8–12 min", "Mon,Wed,Fri,Sun", "16:10", "Europe/London", ["air-rpm"], [], False),
    ("uk-news-words", "News Words", "newswords", "UK", "Vocabulary", "The vocabulary of a public news paragraph, without taking a side", "Adult learners in the UK", "education", "unknown", "crowded", "tutorial", "general_gap", "8–12 min", "Tue,Thu,Sat,Sun", "21:00", "Europe/London", ["ypp-inauthentic", "air-rpm"], [], False),
    ("uk-recall-cards", "Recall Cards", "recallcards", "UK", "Study method", "A spaced-repetition session on paper, then in an app", "Students and career changers", "education", "unknown", "giant", "tutorial", "general_gap", "10–14 min", "Mon,Wed,Fri,Sun", "21:10", "Europe/London", ["air-rpm", "vidiq-niches"], [], False),
    ("uk-portfolio-piece", "Portfolio Piece", "portfoliopiece", "UK", "Career education", "Documenting one work sample so a stranger can follow it", "Career changers", "education", "unknown", "crowded", "tutorial", "general_gap", "12–16 min", "Tue,Thu,Sat,Sun", "19:25", "Europe/London", ["vidiq-niches"], [], False),
    ("uk-story-beat", "Story Beat", "storybeat", "UK", "Interview education", "The STAR structure on a fictional example that is labeled fictional", "People preparing for interviews", "education", "unknown", "giant", "tutorial", "general_gap", "10–14 min", "Mon,Wed,Fri,Sun", "12:35", "Europe/London", ["vidiq-niches"], [], False),
    ("uk-deep-hour", "Deep Hour", "deephour", "UK", "Study habits", "Planning one uninterrupted hour and a shutdown note", "Students and self-taught professionals", "education", "unknown", "giant", "tutorial", "general_gap", "8–12 min", "Tue,Thu,Sat,Sun", "21:20", "Europe/London", ["air-rpm"], [], False),
    ("uk-margin-note", "Margin Note", "marginnote", "UK", "Reading method", "Marking a nonfiction chapter so you can find the claim later", "Adult nonfiction readers", "education", "unknown", "workable", "tutorial", "general_gap", "10–14 min", "Mon,Wed,Fri,Sun", "20:15", "Europe/London", ["air-rpm"], [], False),
    ("uk-tariff-read", "Tariff Read", "tariffread", "UK", "Energy-bill education", "The fields on a UK energy bill and where the tariff name sits", "Households opening an annual statement", "unverified", "unknown", "open", "sourced", "general_gap", "10–14 min", "Tue,Thu,Sat,Sun", "18:25", "Europe/London", ["vidiq-niches", "ypp-inauthentic"], [], False),
    ("uk-loft-first", "Loft First", "loftfirst", "UK", "Home-energy education", "What loft insulation does, and when the job needs a professional", "Homeowners comparing energy upgrades", "unverified", "unknown", "open", "sourced", "general_gap", "10–14 min", "Mon,Wed,Fri,Sun", "10:50", "Europe/London", ["vidiq-niches"], [], False),
    ("uk-standby-draw", "Standby Draw", "standbydraw", "UK", "Home measurement", "Using a consumer plug meter on a lamp, safely", "Curious households", "unverified", "unknown", "open", "hobby", "general_gap", "8–12 min", "Tue,Thu,Sat,Sun", "11:55", "Europe/London", ["vidiq-niches"], [], False),
    ("us-plan-week", "Plan Week", "planweek", "US", "Homeschool planning", "A parent's weekly plan: subjects, materials, and a stop time", "Homeschool parents", "unverified", "modest", "open", "hobby", "homeschool", "12–16 min", "Mon,Wed,Fri,Sun", "09:15", "America/Chicago", ["yt-homeschool", "vidiq-niches"], [], False),
    ("us-read-aloud", "Read Aloud", "readaloud", "US", "Parent reading practice", "How a parent prepares a chapter to read aloud", "Parents, adult audience", "unverified", "modest", "open", "hobby", "homeschool", "10–14 min", "Tue,Thu,Sat,Sun", "20:45", "America/New_York", ["yt-homeschool", "vidiq-niches"], [], False),
    ("us-record-box", "Record Box", "recordbox", "US", "Homeschool records", "A simple box of work samples and a dated index", "Parents who must keep records", "unverified", "modest", "open", "hobby", "homeschool", "10–14 min", "Mon,Wed,Fri,Sun", "14:10", "America/Chicago", ["yt-homeschool"], [], False),
    ("us-lab-safety", "Lab Safety", "labsafetyhome", "US", "Home-science safety", "A parent's checklist before a kitchen science activity", "Parents supervising activities", "unverified", "modest", "open", "sourced", "homeschool", "8–12 min", "Tue,Thu,Sat,Sun", "10:25", "America/New_York", ["yt-homeschool", "ypp-inauthentic"], [], False),
    ("uk-council-page", "Council Page", "councilpage", "UK", "Civic literacy", "How a local council website is usually organized", "Residents trying to find a bin day or a planning notice", "unverified", "unknown", "open", "tutorial", "general_gap", "8–12 min", "Mon,Wed,Fri,Sun", "19:30", "Europe/London", ["vidiq-niches"], [], False),
    ("us-grant-form", "Grant Form", "grantform", "US", "Small-business admin", "How to read a grant form before writing the narrative", "First-time applicants", "education", "unknown", "open", "tutorial", "general_gap", "12–16 min", "Tue,Thu,Sat,Sun", "13:20", "America/Chicago", ["vidiq-niches", "air-rpm"], [], False),
    ("us-vendor-compare", "Vendor Compare", "vendorcompare", "US", "Software buying education", "A three-vendor scorecard with weights written down", "Operators choosing a tool", "education", "steady", "workable", "tutorial", "ai_screen", "12–16 min", "Mon,Wed,Fri,Sun", "15:40", "America/New_York", ["yt-matt", "vidiq-niches"], ["matt"], False),
    ("us-close-week", "Close the Week", "closeweek", "US", "Team operations", "A Friday review for a five-person team: done, stuck, next", "Small-team leads", "education", "unknown", "open", "tutorial", "general_gap", "8–12 min", "Tue,Thu,Sat,Sun", "16:40", "America/Chicago", ["vidiq-niches"], [], False),
]

EXCLUDED = [
    {
        "id": "sensational-macro",
        "reason": "Public search showed very high velocity on fear-and-politics finance videos. That pattern is a poor advertiser fit and a poor match for sourced education.",
    },
    {
        "id": "exploit-demonstrations",
        "reason": "Security content that demonstrates attacks, exploit kits, or intrusion steps is outside this desk.",
    },
    {
        "id": "animal-distress-templates",
        "reason": "YouTube's monetization policy treats repetitive animal peril as off-putting content.",
    },
    {
        "id": "made-for-kids",
        "reason": "Made-for-kids inventory has a separate quality bar and is not part of this network.",
    },
    {
        "id": "music-covers",
        "reason": "Covers and pitch-shifted songs collide with copyright and reused-content rules.",
    },
    {
        "id": "pranks",
        "reason": "Prank formats are a weak advertiser fit and are easy to make unsafe.",
    },
    {
        "id": "scraped-compilations",
        "reason": "Compilations of other people's footage fail the reused-content policy.",
    },
    {
        "id": "ai-expert-personas",
        "reason": "YouTube does not monetize AI personas presented as human experts on health, finance, law, or politics.",
    },
]

VISUAL = {
    "sourced": "Paper, ink, and a large figure. No synthetic face. Citations stay on screen next to the claim.",
    "tutorial": "Full-screen capture, a zoom on the control being used, and a caption that names the click.",
    "hobby": "The object fills the frame. Hands may appear. No stock-footage montage.",
    "food": "Overhead board, a scale, and the finished plate. Recipes are original.",
    "fitness": "A side angle of the movement and a text cue. No before-and-after body imagery.",
    "craft": "The work in progress, then the finished object, on a plain table.",
}

VOICE = {
    "sourced": "Human narrator in the market accent. AI may assist an edit. The video never introduces an AI adviser, doctor, or lawyer.",
    "tutorial": "Human narrator talking through the recording. The software is not given a persona.",
    "hobby": "Calm human narration under the work.",
    "food": "Human cook or narrator. Quantities are spoken as they are weighed.",
    "fitness": "Human coaching cues. No medical claim.",
    "craft": "Quiet human narration.",
}

KEYWORDS = {
    "UK": "United Kingdom, Britain, UK",
    "US": "United States, USA",
}


def _row(raw: tuple) -> dict:
    (
        cid, name, handle, market, category, niche, audience,
        monetization, velocity, competition, policy, dna, duration,
        days, hour_local, tz, evidence, competitors, launch,
    ) = raw
    score = (
        MONETIZATION_POINTS[monetization]
        + VELOCITY_POINTS[velocity]
        + COMPETITION_POINTS[competition]
        + POLICY_POINTS[policy]
    )
    sensitive = category.lower().find("medicare") >= 0 or "finance" in category.lower() or "tax" in category.lower() or "mortgage" in category.lower() or "pension" in category.lower() or "estate" in category.lower() or "debt" in category.lower() or "credit" in category.lower() or "savings" in category.lower() or policy == "sourced"
    return {
        "id": cid,
        "name": name,
        "handle": handle,
        "market": market,
        "category": category,
        "niche": niche,
        "audience": audience,
        "positioning": niche[0].upper() + niche[1:] + f". Made for {audience[0].lower() + audience[1:]}.",
        "monetization_key": monetization,
        "velocity_key": velocity,
        "competition_key": competition,
        "policy_key": policy,
        "dna_key": dna,
        "score": score,
        "score_parts": {
            "monetization": MONETIZATION_POINTS[monetization],
            "cluster_velocity": VELOCITY_POINTS[velocity],
            "competition": COMPETITION_POINTS[competition],
            "policy_fit": POLICY_POINTS[policy],
        },
        "monetization_note": MONETIZATION_NOTE[monetization],
        "duration": duration,
        "publish_days": days,
        "publish_hour_local": hour_local,
        "timezone": tz,
        "schedule_basis": (
            "No audience analytics exist yet. The hour is a planning assumption in the "
            "channel timezone, staggered so the network does not publish in one burst. "
            "Replace it with YouTube Studio audience data after the channel has viewers."
        ),
        "visual": VISUAL[policy],
        "voice": VOICE[policy],
        "keywords": f"{niche}, {KEYWORDS[market]}, {category}",
        "evidence_ids": evidence,
        "competitor_ids": competitors,
        "launch": launch,
        "ai_persona_allowed": False,
        "sensitive_topic": sensitive or policy == "sourced",
        "youtube_created": False,
        "weekly_target": 4,
        "description": (
            f"{name} explains {niche[0].lower() + niche[1:]} for a {market} audience. "
            "Videos are original, sourced, and advertiser-friendly. "
            "They are education, not personal advice."
        ),
    }


def build_channels() -> list[dict]:
    channels = [_row(raw) for raw in RAW]
    channels.sort(key=lambda c: (-c["score"], c["name"]))
    for index, channel in enumerate(channels, start=1):
        channel["rank"] = index
    return channels


CHANNELS = build_channels()


def channel_by_id(channel_id: str) -> dict | None:
    for channel in CHANNELS:
        if channel["id"] == channel_id:
            return channel
    return None


def summary() -> dict:
    markets: dict[str, int] = {}
    for channel in CHANNELS:
        markets[channel["market"]] = markets.get(channel["market"], 0) + 1
    return {
        "channel_count": len(CHANNELS),
        "launch_count": sum(1 for c in CHANNELS if c["launch"]),
        "markets": markets,
        "youtube_channels_created": sum(1 for c in CHANNELS if c["youtube_created"]),
        "videos_published": 0,
        "weekly_goal": 4 * len(CHANNELS),
        "weekly_goal_note": (
            "400 is the owner's stated scale target. It is not the current production "
            "capacity, and it is not a count of finished videos."
        ),
        "retrieved": RETRIEVED,
        "excluded": EXCLUDED,
    }
