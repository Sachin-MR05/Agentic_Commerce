
## 1. What is Still Missing in Agentic Commerce

* **Integration Between LLMs and Deterministic Recommendation Engines:** LLMs are great conversationalists but poor inventory managers. Without real-time integration into live commerce catalogs and recommendation engines, agents surface discontinued SKUs, broken links, incorrect specs, and out-of-stock items.


* **Cryptographic Intent Mandates & Bound Payment Rails:** Agents need standardized protocols (such as Stripe/OpenAI’s ACP or Visa’s TAP) to prove that the consumer explicitly delegated authority to spend within specific bounds (e.g., maximum dollar amounts, specific categories, or time windows).
* **Duty of Loyalty & Conscious Commerce:** AI agents lack built-in safeguards to prove they are acting in the consumer’s best interest. Recent research shows agents can be easily manipulated by prompt injections, sponsored search rankings, or distorted training data rather than selecting the best product for the buyer.
* **Machine-to-Machine Micro-Settlements:** Traditional card rails are poorly suited for cross-border, high-frequency, or micro-transactions between agents, requiring agent-native wallets and KYA (Know Your Agent) frameworks.

---

## 2. What Makes Agentic Commerce Lag in Adoption

* **The Trust and Obfuscation Dilemma:** When an AI agent intermediates a transaction through multiple models and discovery layers, the direct consumer-to-merchant relationship is obscured. Merchants cannot verify whether the intent is genuine or based on stolen credentials, which spikes perceived fraud risk.
* **Bot Managers and Firewall Friction:** Because many agents browse the web like automated scripts, they hit anti-bot defenses (e.g., Forter, Sardine, CAPTCHAs) and receive 403 Forbidden errors before they can even add items to a cart.
* **Consumer Control & Consent Fatigue:** Consumers are skeptical of "full autonomy" for high-consideration purchases. Designers struggle to find a balance between asking for user confirmation at every step (causing consent fatigue) and acting too autonomously (causing anxiety and disputes).


* **Broken Advertising and Monetization Models:** AI agents do not have human eyeballs. The traditional display and search advertising model breaks down, leaving platforms uncertain about how to monetize agentic traffic beyond basic transaction fees.



---

## 3. Where Merchants Fail

| Area of Failure | Why It Happens | Consequence for Agentic Buying |
| --- | --- | --- |
| **Human-Only Interfaces** | Merchant websites are built for human eyes and cursor clicks rather than clean, machine-readable schemas (like ACP, AP2, or MCP servers). | Agents fail at the checkout UI or get blocked as malicious scrapers. |
| **Dirty & Un-normalized Catalogs** | Merchants fail to maintain clean, normalized product feeds with real-time stock levels, return rates, and verified attributes.

 | Agents recommend items that cannot be fulfilled or result in immediate returns.

 |
| **Fear of Disintermediation ("Dumb Pipes")** | Merchants view AI platforms purely as threats that will strip away their customer relationships and brand equity.

 | Merchants react defensively by blocking agents rather than exposing secure, authenticated APIs. |
| **Lack of First-Party Agentic Front-Ends** | Merchants rely solely on external third-party chat platforms instead of building native agentic shopping assistants on their own sites.

 | Merchants lose the discovery phase entirely and surrender margin to third-party gatekeepers.

 |

---
