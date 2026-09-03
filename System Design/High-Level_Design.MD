                           ┌─────────────────────┐
                           │    HUMAN BUYER      │
                           │                     │
                           │ Login / OTP / Auth  │
                           └──────────┬──────────┘
                                      │
                                      ▼
                              Existing Store UI
                                      │
                                      │
                                      ▼
                              Merchant Dashboard
                                      │
                                      ├── AI Monitoring
                                      ├── Audit Trail
                                      ├── Decision Explanations
                                      ├── Pending Approvals
                                      └── Failure Monitoring


                           ┌─────────────────────┐
                           │    AI BUYER AGENT   │
                           └──────────┬──────────┘
                                      │
                           Agent-to-Agent Protocol
                                      │
                             mTLS / Secure Channel
                                      │
                                      ▼
                 ┌────────────────────────────────────┐
                 │          AGENT GATEWAY              │
                 │                                    │
                 │ Agent Identity Verification        │
                 │ Authentication                     │
                 │ Authorization                      │
                 │ Scoped, Time-Bound Tokens          │
                 │ Request Signature / Integrity      │
                 │ Replay Protection                  │
                 │ Rate Limiting                      │
                 │                                    │
                 │ Token Scope: catalog / order /    │
                 │ payment operations                 │
                 └─────────────────┬──────────────────┘
                                   │
                                   ▼
                 ┌────────────────────────────────────┐
                 │          MERCHANT AGENT             │
                 │                                    │
                 │ LLM / Reasoning                    │
                 │ Requirement Understanding          │
                 │ Negotiation                        │
                 │ Tool Orchestration                 │
                 │                                    │
                 │ LLM CAN ONLY PROPOSE ACTIONS       │
                 └─────────────────┬──────────────────┘
                                   │
                              Proposed Action
                                   │
                                   ▼
                 ┌────────────────────────────────────┐
                 │          POLICY ENGINE              │
                 │                                    │
                 │ Discount Limits                    │
                 │ Order Value Limits                 │
                 │ Quantity Limits                    │
                 │ Approval Thresholds                │
                 │ Allowed Operations                 │
                 └───────────────┬───────────┬────────┘
                                 │           │
                              ALLOW       APPROVAL
                                 │           │
                                 │           ▼
                                 │   ┌──────────────────┐
                                 │   │ HUMAN APPROVAL   │
                                 │   │                  │
                                 │   │ Approve / Reject │
                                 │   └────────┬─────────┘
                                 │            │
                                 │       ┌────┴────┐
                                 │       ▼         ▼
                                 │    APPROVE    REJECT
                                 │       │
                                 │       │
                                 │       ▼
                                 │   TIMEOUT
                                 │       │
                                 │       ▼
                                 │  AUTO-REJECT
                                 │       │
                                 └───────┬┘
                                         │
                                         ▼
                              Buyer Agent Notified
                                         │
                                         ▼
                 ┌────────────────────────────────────┐
                 │       TOOL / ADAPTER LAYER          │
                 │                                    │
                 │ Catalog Tool                       │
                 │ Inventory Tool                     │
                 │ Pricing Tool                       │
                 │ Order Tool                         │
                 │ Payment Tool                        │
                 │                                    │
                 │ Payment Tool ONLY AVAILABLE        │
                 │ AFTER POLICY-APPROVED ORDER        │
                 └─────────────────┬──────────────────┘
                                   │
                                   ▼
                 ┌────────────────────────────────────┐
                 │      EXISTING MERCHANT BACKEND     │
                 │                                    │
                 │ Products                           │
                 │ Inventory                          │
                 │ Orders                             │
                 │ Customers                          │
                 │ Database                           │
                 └───────────────┬────────────────────┘
                                 │
                            Completed Order
                                 │
                                 ▼
                 ┌────────────────────────────────────┐
                 │          PAYMENT SERVICE             │
                 │                                    │
                 │        Razorpay Test API           │
                 │                                    │
                 │ Payment only for approved order    │
                 └─────────────────┬──────────────────┘
                                   │
                                   ▼
                                PAYMENT


       ┌──────────────────────────────────────────────────────────┐
       │                    FAILURE HANDLER                        │
       │                                                          │
       │ Insufficient Stock → Explain + No Order                  │
       │ Policy Violation    → Block + Notify                     │
       │ Approval Timeout    → Reject + Notify                    │
       │ Approval Rejected   → Cancel + Notify                    │
       │ Payment Failure     → PAYMENT_FAILED + Notify            │
       │ API Timeout         → Controlled Retry / Failure         │
       └──────────────────────────────────────────────────────────┘


       ┌──────────────────────────────────────────────────────────┐
       │                     AUDIT SERVICE                         │
       │                                                          │
       │ Append-Only / Write-Only                                 │
       │                                                          │
       │ Agent Requests                                           │
       │ Agent Decisions                                           │
       │ Policy Decisions                                          │
       │ Offers                                                   │
       │ Approval Requests / Results                              │
       │ Orders                                                   │
       │ Payments                                                 │
       │ Failures                                                 │
       │ Decision Explanations                                    │
       │                                                          │
       │ Components can APPEND only.                              │
       │ Past audit records cannot be modified or deleted.        │
       └────────────────────────┬─────────────────────────────────┘
                                │
                                ▼
       ┌──────────────────────────────────────────────────────────┐
       │               AI COMMERCE MONITORING                      │
       │                       DASHBOARD                           │
       │                                                          │
       │ Live Agent Activity                                      │
       │ Active Transactions                                      │
       │ Pending Approvals                                       │
       │ Decision Explanations                                   │
       │ Complete Audit Trail                                    │
       │ Successful Payments                                     │
       │ Failed Transactions                                     │
       │ Failure Reasons / Recovery                              │
       └──────────────────────────────────────────────────────────┘