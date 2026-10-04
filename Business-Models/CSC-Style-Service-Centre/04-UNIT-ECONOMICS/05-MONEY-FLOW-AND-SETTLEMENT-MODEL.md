# Money Flow & Settlement Model

## Purpose
Define how customer money, service-provider cost, centre/VLE commission, partner share and central margin should be tracked.

## Generic flow
Customer payment
→ transaction/service ledger
→ taxes/regulated charges where applicable
→ service/provider cost
→ centre/VLE share
→ distributor/territory share where contractually applicable
→ central/platform margin
→ incentives/reinvestment
→ settlement/reconciliation.

## Important CSC research rule
Do not assume one universal percentage for every CSC service. The official CSC/VLE revenue-sharing framework and individual service/provider schedules must be separated. Service-wise and state-wise evidence must be recorded independently.

## Required fields
Transaction ID | Service | State | Centre ID | Partner ID | Customer fee | Provider cost | Taxes/charges | VLE share | Distributor/territory share | Central share | Settlement date | Refund/adjustment | Source.

## Nivy design principle
Prefer transparent digital settlement and a ledger/dashboard over informal cash sharing.

## Franchise fee
Keep one-time franchise/partner fee separate from recurring service economics. Do not use joining fees as the primary proof of business sustainability.
