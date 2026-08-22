Agentic Commerce:

AI agents can discover products, make decisions, and complete purchases on behalf of a user—with the user's permission—without the user manually going through a traditional ecommerce checkout.

Traditional ecommerce: Human → Website → Product → Cart → Checkout → Payment
Agentic commerce: Human → AI Agent → Merchant → Payment → Order

need for agentic commerce
Traditional ecommerce was designed for humans clicking through websites. AI agents are starting to act on behalf of humans, so commerce systems need a way for those agents to safely discover, buy, pay, and track orders.

------------------------------------
Sheetal Lalwani, Co-founder & Chief Operating Officer JUSPAY explains at Visa Payments in Motion:Commercial Edition.

AI will have a bigger impact on B2B commerce
    B2B commerce is more suitable for AI than consumer/retail commerce.

    B2B transactions are complicated:

Multiple approval levels
Multiple departments
Complex business processes
Procurement workflows
Human decision-making
Large amounts of unstructured information

AI is good at:

Understanding unstructured data
Automating repetitive workflows
Making decisions/recommendations
Connecting multiple processes
Keeping humans involved where necessary

Main idea:

The more complicated the business workflow, the more valuable AI agents become.

AI agents will start doing B2B commerce

If an AI agent is capable of buying something, how does it actually pay?

Traditional payment methods aren't necessarily designed for autonomous software agents.

That's where he introduces:

Commercial cards → Virtual cards → Programmable money

A virtual commercial card can potentially be:

Created for a specific transaction
Limited to a certain amount
Limited to a particular merchant
Limited to a particular category
Controlled by business rules
Used by an AI agent without exposing the company's main card

So the payment instrument becomes programmable.

4. Virtual cards are like "programmable money"

Traditional card

Company gives employee a card → employee decides what to purchase → payment happens.

AI + virtual card

Company gives AI agent controlled payment capability → AI decides/executes according to rules → virtual card performs payment.

5. Visa is betting heavily on this

Because if agentic commerce becomes widespread, every AI-driven business transaction could eventually require a payment mechanism.

That creates opportunities for Visa in:

Payment rails
Commercial cards
Virtual cards
Tokenization
Security
Fraud prevention
Compliance
AI-agent payment infrastructure

So Visa doesn't necessarily need to build the AI agent itself.

7. Three major players need to work together

A. Networks

Examples: Visa, Mastercard

Their responsibility:

Payment rails
Network infrastructure
Security
Standards
Trust
Authentication
Transaction processing
B. Banks

They provide:

Credit
Commercial accounts
Cards
Account relationships
Risk management
Compliance
C. Fintech companies

They make everything easier for businesses.

For example:

Better APIs
Developer platforms
AI payment products
Virtual-card platforms
Automation
User-friendly interfaces

---------------------------------------
where does the AI get the product information and company APIs?

| Data                        | Example                                        | Source                                  |
| --------------------------- | ---------------------------------------------- | --------------------------------------- |
| Product requirements        | "Need 500 sensors, -20°C to 150°C"             | Employees / purchase team               |
| Existing products           | Product name, specs, SKU, price                | Company catalog / suppliers             |
| Supplier data               | Supplier, location, reliability, payment terms | Supplier onboarding                     |
| Inventory                   | Current stock, reorder level                   | ERP/WMS                                 |
| Purchase history            | What was bought, from whom, when               | ERP / procurement system                |
| Human knowledge             | Staff notes, feedback, complaints              | Employees / CRM / tickets               |
| External products           | New products, prices, specifications           | Supplier websites / APIs / marketplaces |
| External market information | New suppliers, product launches                | Web                                     |
---------------------------------------------
https://www.youtube.com/watch?v=LtFCXOOGPrw

Major Issues and Challenges Discussed
Trust, Fraud, and Obfuscation: When an agent acts as an intermediary, it obfuscates the direct relationship between the consumer and the merchant [14:09]. Merchants struggle to verify if the consumer intent is valid or if the credentials are stolen, leading to immense fraud risks [15:15].

Bot Blockers and Access: Currently, agents traverse the web similarly to human shoppers, which causes them to be blocked by standard bot managers (like Forter or Sardine) that protect merchants from malicious scraping [35:48].

Agent Loyalty and Manipulation: Since AI agents lack human intuition, there is a risk they can be manipulated by sponsored labels, prompt injections, or biased training data, leading them to act against the consumer's best interests [50:42].

Consent Fatigue vs. Autonomy: Striking the right balance between giving the AI enough autonomy to be useful, while ensuring it adheres strictly to the user's intent without constantly bombarding them for approval [27:19].

Disruption of the Advertising Model: Agents "don't have eyeballs," meaning the traditional ad-funded internet model is fundamentally broken in an agentic workflow [34:36].

Solutions & Protocols
To address these challenges, the panel highlighted several emerging protocols and systems:

1. Stripe & OpenAI: Agentic Commerce Protocol (ACP)

Shared Payment Tokens: To allow checkouts and inventory to be legible to AI, ACP acts as a shared language between agents and sellers [06:22]. Stripe uses "Shared Payment Tokens" to securely package a user's payment credentials without exposing the raw card number to the seller or forcing the agent to take on merchant liabilities [07:33].

Real-time Risk Scoring: The token is integrated with Stripe Radar to score transactions for fraud in real-time [09:33].

2. Visa: Trusted Agent Protocol (TAP)

Cryptographic Passports: Visa's TAP provides agents with a cryptographic passport so merchants can verify they are legitimate delegates of a real consumer [18:18].

Bank-Verified Tokens & Intent Logging: The protocol tokenizes credentials validated directly by the card-issuing bank [21:21]. It also logs the consumer's specific "payment instruction" (e.g., spending limits or categories), ensuring the agent cannot spend beyond the predetermined boundaries [24:26].

3. Skyfire: Know Your Agent (KYA) and Wallets

Agent Economic Identity: Skyfire approaches the problem by giving agents their own funded wallets to handle microtransactions, particularly across borders where traditional credit cards fail due to low transaction values [34:55].

Bypassing Bot Blockers: They use "Know Your Agent" (KYA) identity payloads. By delivering a verified identity package showing exactly which principal (user) the agent represents, agents are safely granted access to merchant sites past the 403 bot blockers [38:23].

4. Consumer Reports: "Conscious Commerce"

Ensuring Loyalty: Consumer Reports emphasized building systems to evaluate and measure an agent's true loyalty to the consumer [48:49].

Value-Driven Purchasing: "Conscious commerce" involves making sure that the values a consumer cares about (e.g., budget, sustainability, labor practices) are accurately reflected in the agent's intent and final purchase, without being swayed by hidden vendor manipulation [49:55].



--------------------
https://www.youtube.com/watch?v=LtFCXOOGPrw&t=1416s

The Key Ideas: Evolution, Not Elimination
The Myth of Monoculture: The end-to-end shopping experience will not be monopolized by a single platform. Historically, digital channels fragment and add to the ecosystem rather than replace existing ones (e.g., e-commerce grew the overall retail pie rather than entirely cannibalizing brick-and-mortar).

Upper-Funnel Dominance: Currently, AI agents have achieved massive product-market fit at the top of the funnel (discovery and complex problem-solving) because they remove major friction points.

Retail Media is Durable: Agentic platforms will elevate retail media, not destroy it. Consumers value the context and equity of shopping directly with trusted brands and retailers.

Skepticism on "Full Autonomy": The speaker predicts that fully autonomous purchasing (where the agent buys completely on its own) is unlikely to gain mass adoption. Low-consideration items don't require complex AI, and consumers want control over high-consideration purchases.

Major Issues and Challenges
The Lower-Funnel Gap: Agentic platforms currently struggle with mid-to-lower funnel tasks (consideration and purchase). They lack the real-time, deterministic data required to close a sale effectively.

The Data Quality Problem (The "Bike Tire" Dilemma): LLMs are great conversationalists but terrible inventory managers. When left to their own devices, agents often surface broken links, out-of-stock items, discontinued products, or factually incorrect product specs.

Monetization Uncertainty: It remains unclear how AI platforms will scale their revenue. While marketplaces and transaction fees (like OpenAI's Instant Checkout) are being tested, native advertising remains the most historically scalable path, provided it can be adapted to an agentic interface.

Retailer Disintermediation: If retailers surrender the agentic discovery phase to third-party AI platforms, they risk losing their direct relationship with the consumer and becoming "dumb pipes."


Solution,How It Works,Strategic Impact
LLM + Recommendation Engine Integration,"The conversational LLM acts as the front-end, but queries a dedicated, real-time commerce database (like Criteo's catalog) for the actual product data.","Solves the data quality problem by ""normalizing"" subjective terms and surfacing only in-stock, highly relevant, and accurate SKUs."
New Transactional Integrations,"Initiatives like OpenAI's Instant Checkout partner directly with blue-chip brands (Etsy, Shopify, Walmart) to close the loop natively.","Gives AI platforms the transactional data feeds they desperately need to improve lower-funnel algorithms, while giving merchants incremental demand."
First-Party Retailer Agents,Retailers must build their own best-in-class agentic front-ends directly on their e-commerce sites.,Protects the retailer's traffic and ensures they own the customer journey from discovery to checkout.
Contextual Agentic Advertising,"Redefining native ads so that ""visibility is the ad."" Brands pay to be part of the agent's highly accurate, data-backed consideration set rather than relying on flashing banners.","Provides a durable, scalable monetization model for agentic platforms without ruining the user experience."

------------------------------------
youtube.com/watch?v=ths73hH6yoc&sttick=0

The Dawn of Agentic Commerce
The Paradigm Shift: E-commerce is evolving from traditional search-and-click to AI-driven in-chat purchasing. Consumers will soon bypass dedicated stores and buy directly through LLMs like ChatGPT and Gemini.

New Open Standards: Innovations like the Agentic Commerce Protocol (ACP) (developed by OpenAI and Stripe) and Anthropic's Model Context Protocol (MCP) are creating the shared language for machines to securely transact with businesses.

Massive Economic Impact: A McKinsey report projects that agentic commerce could drive $1 trillion in the US B2C retail market and up to $3 to $5 trillion globally by 2030.

Multi-Vendor Bundling: Agents will have the power to seamlessly bundle products from completely different sellers into a single, unified transaction for the buyer.

Major Challenges & Issues
The Death of Traditional SEO: Optimizing keywords for Google or Amazon is no longer enough. Brands that rely solely on legacy SEO and traditional ad budgets risk becoming completely invisible to AI agents.

The "Scraping" Lag: Early AI models relied on periodic web scraping, which resulted in outdated inventory, broken links, and inaccurate pricing for merchants.

The Threat to Marketplaces: Major platforms face a massive existential threat as younger generations increasingly begin their purchase journeys directly in AI tools rather than traditional search engines.

Technical Burdens: Brands that lag in technology will struggle to format their massive, complex catalogs into the strict, machine-readable schemas required to participate in this new ecosystem.

Solutions & Strategic Actions
To survive and thrive, Jacob emphasizes that brands must fundamentally change how they expose their data to the internet:

Adopt Structured Data: Brands must publish their catalogs using strict, machine-readable formats (like OpenAI's product feed specs, which require detailed fields for GTIN, dimensions, variants, compliance, and geotagging).

Implement Real-Time Feeds: Moving away from static web scraping, brands need live API connections (like ACP) so agents have 24/7 access to accurate pricing and inventory.

Build Algorithmic Trust: AI agents do not care about flashy banners; they care about verifiable facts. Brands must build trust through clear descriptions, authentic reviews, and highly reliable data feeds.

Note: Getting your brand integrated into these AI search engines early offers a massive opportunity for early-adopter traffic and new revenue streams before the space gets incredibly crowded.

------------------------