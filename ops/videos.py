"""Launch-batch packages. State stays script_ready until a master file exists."""

from __future__ import annotations

VIDEOS = [
    {
        "id": "salary-ledger-ep1",
        "channel_id": "uk-salary-ledger",
        "state": "script_ready",
        "title": "The £20,000 ISA allowance is a cap, not a target",
        "titles": [
            "The £20,000 ISA allowance is a cap, not a target",
            "What actually changes when a UK salary rises",
            "Workplace pension first, ISA second: a worked example",
            "Cash ISA versus stocks and shares ISA after April 2027",
            "Three salaries, one allowance, zero product picks",
        ],
        "description": (
            "The 2026/27 ISA allowance on GOV.UK is £20,000. This original episode "
            "treats that figure as a cap and walks through three labeled illustrations. "
            "From 6 April 2027 the cash ISA limit for people under 65 changes. "
            "Not financial advice.\n\n"
            "https://www.gov.uk/individual-savings-accounts\n"
            "https://www.gov.uk/government/publications/tax-free-savings-newsletter-23/tax-free-savings-newsletter-23-september-2026"
        ),
        "tags": ["ISA", "UK personal finance", "workplace pension", "cash ISA", "stocks and shares ISA"],
        "hashtags": ["#ISA", "#UKMoney", "#PersonalFinance"],
        "category": "Education",
        "made_for_kids": False,
        "script": "content/scripts/uk-salary-ledger.md",
        "playlist": "Salary bands",
        "captions": "No caption file. Narration has not been recorded.",
        "endscreen": "Unassigned until a second finished episode exists.",
    },
    {
        "id": "drawdown-desk-ep1",
        "channel_id": "uk-drawdown-desk",
        "state": "script_ready",
        "title": "A pension pot is not a paycheck",
        "titles": [
            "A pension pot is not a paycheck",
            "Drawdown and annuity are different machines",
            "Write the assumption down before the income number",
            "Why a US study is not a UK guarantee",
            "Three pots, three questions, no product",
        ],
        "description": (
            "Original episode on the difference between a pension balance and a monthly "
            "income. Assumptions are labeled. A headline rate is not a quote. "
            "Not financial advice.\n\n"
            "https://www.moneyhelper.org.uk/en/pensions-and-retirement\n"
            "https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/lifeexpectancies"
        ),
        "tags": ["UK pension", "drawdown", "annuity", "retirement income"],
        "hashtags": ["#UKPension", "#Retirement"],
        "category": "Education",
        "made_for_kids": False,
        "script": "content/scripts/uk-drawdown-desk.md",
        "playlist": "Retirement questions",
        "captions": "No caption file. Narration has not been recorded.",
        "endscreen": "Unassigned until a second finished episode exists.",
    },
    {
        "id": "bench-test-ep1",
        "channel_id": "us-bench-test",
        "state": "script_ready",
        "title": "Test one AI writing tool on one brief, and keep the client's name out of it",
        "titles": [
            "Test one AI writing tool on one brief, and keep the client's name out of it",
            "A 30-minute bench for any new AI writing tool",
            "Stop pasting real customer emails into a demo",
            "The scorecard has four lines and no leaderboard",
            "What a screen recording must show before you trust a draft",
        ],
        "description": (
            "A method for testing an AI writing tool on a fictional brief. "
            "The scorecard is fidelity, constraint, residue, and time. "
            "Not a product ranking and not legal advice."
        ),
        "tags": ["AI tools", "workflow", "screen recording", "writing tools"],
        "hashtags": ["#AIWorkflow", "#Tutorials"],
        "category": "Education",
        "made_for_kids": False,
        "script": "content/scripts/us-bench-test.md",
        "playlist": "One-brief benches",
        "captions": "No caption file. Narration has not been recorded.",
        "endscreen": "Unassigned until the second editor episode exists.",
    },
    {
        "id": "coverage-map-ep1",
        "channel_id": "us-coverage-map",
        "state": "script_ready",
        "title": "Original Medicare, Medicare Advantage, and Medigap are three different structures",
        "titles": [
            "Original Medicare, Medicare Advantage, and Medigap are three different structures",
            "How to read the Medicare.gov coverage page without picking a plan",
            "Medigap letters are standardized. The price is not.",
            "You do not use Medigap to pay a Medicare Advantage bill",
            "A map of the choice, with the ZIP code left blank",
        ],
        "description": (
            "Reads the public Medicare.gov pages on Original Medicare, Medicare Advantage, "
            "and Medigap. 2026 figures are taken from the Medigap letter chart. "
            "Not medical or insurance advice.\n\n"
            "https://www.medicare.gov/basics/get-started-with-medicare/get-more-coverage/your-coverage-options\n"
            "https://www.medicare.gov/health-drug-plans/medigap/basics/compare-plan-benefits"
        ),
        "tags": ["Medicare", "Medigap", "Medicare Advantage", "Original Medicare"],
        "hashtags": ["#Medicare", "#Medigap"],
        "category": "Education",
        "made_for_kids": False,
        "script": "content/scripts/us-coverage-map.md",
        "playlist": "Medicare structures",
        "captions": "No caption file. Narration has not been recorded.",
        "endscreen": "Unassigned until the letter-chart episode exists.",
    },
]


def videos_for(channel_id: str) -> list[dict]:
    return [video for video in VIDEOS if video["channel_id"] == channel_id]
