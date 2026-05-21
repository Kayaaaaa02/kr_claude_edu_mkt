# F&F CN Claude Code Workshop Script - English

> Source file: `cn_claude_edu.html`
> Purpose: Detailed presenter script for walking through the page
> Tone: Practical, business-oriented, executive-friendly, beginner-aware

---

## 0. Top Navigation

**Page Area:** Top Navigation  
**HTML Reference:** `<header class="top-nav">`  
**Visible Section:** F&F · CN logo, Overview, Plan Framework, Scenario A, Hands-on, Deploy, Korean/English toggle, Workshop PDF, Start Workshop

Good morning, everyone. Today we will run a practical Claude Code workshop for the F&F China team, focused on building a business-ready dashboard from data and extending that output into a report workflow.

The top navigation shows the overall structure of today's session. We will begin with the workshop overview, move into the planning framework, work through Scenario A, complete the hands-on build, and then connect the output to PowerPoint reporting and internal deployment through DCS AI.

On the right side, you will see the Korean and English language toggle. The page is available in both languages, so participants can reference the version that is most comfortable for them. The session will be delivered primarily in Korean, but the key business and technical terms will be reinforced in English as well.

---

## 1. Hero Opening

**Page Area:** Hero  
**HTML Reference:** `<section class="hero">`  
**Visible Section:** “Build Your Own Dashboard”

The core message of today's workshop is simple.

We will build one connected workflow from data, to dashboard, to business report.

What we are creating today is not just a sample page. It is a practical workflow that reflects real recurring work: checking data, reviewing performance, building a clear screen, preparing a report, and sharing the result with the organization.

For participants who are new to Claude Code, we will use one sample dataset and one guided scenario. By the end of the session, the goal is for each participant to understand how to produce one working dashboard and one report-ready PowerPoint output.

The important point is not how much code you already know. The important point is how clearly you can define the business objective, the data, the report audience, and the direction Claude should follow.

---

## 2. Key Metrics Summary

**Page Area:** Stat Strip  
**HTML Reference:** `<div class="stat-strip">`  
**Visible Section:** 120 minutes, 1 scenario, 2 outputs, 5-step PLAN

Today's workshop is designed as a 120-minute practical session.

We will not cover many disconnected topics at a shallow level. Instead, we will follow one hands-on scenario deeply and complete the end-to-end workflow.

There are two target outputs. The first is a dashboard. The second is a PowerPoint report generated from the core insights in that dashboard.

The starting point for the entire workflow is the five-step PLAN worksheet. This PLAN determines the quality of the final result. Rather than asking AI to “just build something,” we will first define the purpose, data, screen structure, report format, and deployment method.

---

## 3. Run-of-Show

**Page Area:** Run-of-Show  
**HTML Reference:** `<section class="block" id="ros">`  
**Visible Section:** “A 120-minute journey across 7 chapters”

Let us first review the full flow.

Today's session is organized into seven chapters.

In Opening, we will check the environment and preview the outputs. In Use Case, we will briefly review F&F Korea examples and the core Claude Code mechanisms.

In the PLAN stage, we will design the dashboard before writing code. We will define what decision the dashboard supports and what the screen needs to communicate.

In the Skill Tour, we will learn how to avoid generic AI-looking design and produce a dashboard that feels credible for business use.

In Hands-on 1, we will implement the dashboard using the sample data. In Hands-on 2, we will extend the result into a PowerPoint report and introduce deeper automation concepts using Agent and Hook patterns.

Finally, we will cover how to share and deploy the output securely inside the company environment through DCS AI.

---

## 4. Opening: Setup Check

**Page Area:** Chapter 00  
**HTML Reference:** `<section class="chapter-section" id="ch0">`  
**Visible Section:** “Use the first 10 minutes to remove blockers before hands-on work begins.”

We will begin by checking the practice environment.

This step is short, but it is important. In hands-on sessions, most early blockers are not caused by the code itself. They usually come from environment setup. Before we begin implementation, we need to make sure everyone is starting from the same baseline.

Please confirm that the `claude` command runs successfully from your terminal.

Then confirm that the plugin marketplace command is recognized.

Also confirm that the sample data file, `sample_data.xlsx`, is available.

If anything does not work, please raise your hand immediately. Resolving setup issues now will prevent delays during the dashboard implementation stage.

### 4-1. Initial Readiness Check

**Page Area:** Chapter 00 / 0-A  
**HTML Reference:** `#ch0` / `0-A Initial Readiness Check`

Let us go through the checklist together.

First, confirm that typing `claude` in the terminal starts Claude Code successfully.

Second, confirm that `/plugin marketplace add obra/superpowers-marketplace` is recognized.

Third, confirm that `sample_data.xlsx` has been downloaded.

These three items are required for a smooth hands-on session.

### 4-2. Session Deliverables

**Page Area:** Chapter 00 / 0-B  
**HTML Reference:** `#ch0` / `0-B Session Deliverables`

By the end of the session, you should have two practical outputs.

The first is your own dashboard. We will use sample data today, but the structure can be applied directly to real business data.

The second is an automatically generated PowerPoint report. This report will translate the key insights from the dashboard into a format suitable for executive reporting or team sharing.

---

## 5. Use Case and Claude Code Core Concepts

**Page Area:** Chapter 01  
**HTML Reference:** `<section class="chapter-section" id="ch1">`  
**Visible Section:** “Start with the output. Keep the concepts concise.”

Now let us look at why this workflow matters through actual use cases.

When learning an AI tool, starting with abstract concepts can make it difficult to connect the tool to real work. Today, we will start from the output first and then briefly cover the concepts that make the output possible.

### 5-1. F&F Korea Use Cases

**Page Area:** Chapter 01 / 1-1  
**HTML Reference:** `#ch1` / `F&F Korea Use Cases`

F&F Korea is already using HTML-based reports and dashboards as business outputs.

Traditionally, teams would organize data in Excel, copy content into PowerPoint, and then spend additional time adjusting the design. That process is repetitive, and every data update can require rebuilding the report.

HTML-based dashboards change that workflow. Data, screen, and report can be connected in one reusable structure.

The example links on the page show completed report materials. Today, we will learn how to create this type of output ourselves.

### 5-2. Claude Code Extension Mechanisms

**Page Area:** Chapter 01 / 1-2  
**HTML Reference:** `#ch1` / `Claude Code Extension Mechanisms`

Claude Code includes several extension mechanisms.

The most important one for today is Skills.

Skills are task-specific instruction sets. You can think of them as operating manuals that tell Claude how to approach a specific type of work, such as designing dashboards or creating presentation reports.

Plugins are installable packages that bundle multiple skills or tools together. Today, we use them mainly for workshop setup.

Memory helps Claude remember project or organization preferences. MCP connects Claude Code to external systems. Hooks trigger automated actions before or after specific work steps.

Today, we will actively use Skills and Plugins, while understanding Memory, MCP, and Hooks as concepts for the next level of automation.

---

## 6. PLAN Framework

**Page Area:** Chapter 02  
**HTML Reference:** `<section class="chapter-section" id="ch2">`  
**Visible Section:** “Before execution, a five-minute plan determines the quality of the full deliverable.”

This is the most important planning stage in today's workshop.

The most common mistake when using AI is asking it to implement immediately. If we simply say, “Build a sales dashboard,” Claude may generate a screen, but it may not reflect the business purpose, the decision context, or the most important data.

That is why we start with PLAN.

This PLAN is not just a note. It is a business design brief that directly affects the quality of the output.

### 6-1. Five-Step PLAN Worksheet

**Page Area:** Chapter 02 / Five-Step PLAN Worksheet  
**HTML Reference:** `#ch2` / `Five-Step PLAN Worksheet`

The PLAN worksheet is built around five questions.

First, define the objective. Who will use this dashboard, when, and for what decision?

Second, define the data. What data will be used, where does it come from, and what format is it in?

Third, sketch the screen. Identify the 3 to 5 core indicators that must appear on the screen.

Fourth, define the report format. Is the final output HTML, PowerPoint, or Excel?

Fifth, define the deployment method. Will this remain on your PC, be shared through a URL, or be uploaded to an internal system?

Once these five items are clear, Claude Code can produce a much more accurate result.

### 6-2. Plan Mode

**Page Area:** Chapter 02 / 2-1  
**HTML Reference:** `#ch2` / `How to plan: Plan Mode`

The key feature here is Plan Mode.

When Plan Mode is on, Claude does not write code immediately. It first shows the work plan, and implementation begins only after the user approves it.

This is especially useful for new users because it allows us to review the direction before files are created or modified.

In today's workshop, we will use Plan Mode whenever possible.

In the VS Code extension, press `Shift + Tab` twice to enter Plan Mode. In the terminal, type `/plan` to switch modes.

---

## 7. Recommended Scenario

**Page Area:** Scenario Section  
**HTML Reference:** `<section class="block" id="scenarios">`  
**Visible Section:** “Recommended scenario: follow this path for hands-on work.”

Today's recommended scenario is a weekly sales dashboard for Tmall and Douyin.

This reflects a common workflow in the fashion business: reviewing channel sales, checking week-over-week performance, and identifying which products and categories are driving results.

We will use `sample_data.xlsx`. If you use real business data later, the same structure can be applied to sales data from the Knowledge Graph or other internal sources.

The core indicators are:

First, week-over-week growth rate.

Second, the top 10 products by sales.

Third, a category-by-channel heatmap.

Fourth, weekly sales performance by channel.

These are not decorative charts. They are decision-support indicators for reviewing channel ROI every Monday.

### 7-1. Sample Prompt

**Page Area:** Scenario Section / Sample Prompt  
**HTML Reference:** `#scenarios` / `Sample Prompt - Start with Plan Mode`

A good prompt should not end with “build a dashboard.”

First, state the objective. In this case, the dashboard is for reviewing channel ROI every Monday.

Then specify the core indicators: weekly sales by channel, week-over-week growth, top 10 products, and the category-by-channel heatmap.

Next, suggest chart types such as bar, line, and heatmap.

Finally, define the visual direction. For example, avoid generic AI styling and make the dashboard minimal and business-ready.

With this structure, Claude will present a design plan first. After we review and approve the plan, it will proceed to implementation.

---

## 8. Claude Code Concept Deep-Dive

**Page Area:** Concepts Deep-Dive  
**HTML Reference:** `<section class="chapter-section" id="ch2b">`  
**Visible Section:** “The 5 core features of Claude Code, explained in business terms.”

Before we move deeper into hands-on work, let us align on five core concepts.

Skills are operating manuals. They tell Claude how to handle a certain type of work.

Plugins are bundled installations. They help install multiple skills or tools together.

Memory is a persistent note. It helps Claude remember organizational tone, project preferences, and repeated instructions.

Hooks are automation triggers. They run predefined actions before or after certain workflow steps.

MCP is the connection layer to external systems. It allows Claude Code to connect with company systems, databases, Slack, Figma, or other approved tools.

Today, we will directly use Skills and Plugins. The other concepts prepare us for more advanced automation.

---

## 9. Applying Skills and Improving Design Quality

**Page Area:** Chapter 03  
**HTML Reference:** `<section class="chapter-section" id="ch3">`  
**Visible Section:** “Use Skills to create a business-ready dashboard design.”

Now we will look at how to improve dashboard design quality using Skills.

If we ask AI to design a dashboard without specific direction, the output often looks generic: purple gradients, rounded cards, excessive shadows, and familiar dashboard patterns.

A business dashboard should not only look polished. It should be reliable, readable, and suitable for repeated use.

That is why we use the `frontend-design` skill.

### 9-1. Four Ways to Avoid a Generic AI Result

**Page Area:** Chapter 03 / 3-1  
**HTML Reference:** `#ch3` / `Four ways to avoid a generic AI result`

The first strategy is to explicitly activate the `frontend-design` skill.

Add a line such as, “Use the frontend-design skill actively.” This helps Claude consider layout, color, spacing, typography, and hierarchy more systematically.

The second strategy is to provide a concrete reference. Instead of saying “make it beautiful,” point to a specific website, dashboard, brand guide, or screenshot.

The third strategy is to define the brand tone. Words such as minimal, classic, street, premium, or outdoor casual help maintain consistency.

The fourth strategy is to provide bad and good examples. When Claude sees what to avoid and what to follow, the output direction becomes much clearer.

---

## 10. Hands-on 1: Dashboard Implementation

**Page Area:** Chapter 04  
**HTML Reference:** `<section class="chapter-section" id="ch4">`  
**Visible Section:** “From data to a working screen.”

Now we move into implementation.

In this step, we will analyze the sample data and create a single-file HTML dashboard based on the PLAN we prepared earlier.

The process has four steps.

First, write the PLAN and confirm the direction.

Second, check the data and run the first prompt. Place `sample_data.xlsx` in the working folder so Claude Code can access it.

Third, build and refine the screen. The first draft does not need to be perfect. We will improve the layout, charts, wording, color, and information priority through iteration.

Fourth, perform a quality check. Make sure the numbers are readable, the charts support the decision, and Chinese fonts render correctly.

### 10-1. Scenario Prompt Template

**Page Area:** Chapter 04 / Scenario Prompt Template  
**HTML Reference:** `#ch4` / `Scenario Prompt Template`

The prompt should be specific.

Ask Claude to analyze `sample_data.xlsx` and create a single-file HTML weekly sales dashboard for reviewing channel ROI every Monday.

Specify the core metrics: weekly sales by channel, week-over-week growth rate, top 10 products, and a category-by-channel heatmap.

Specify the chart types: bar, line, and heatmap.

Specify the style direction: minimal, business-ready, and not generic AI styling.

Finally, explicitly ask Claude to use the `frontend-design` skill and `xlsx` skill.

---

## 11. Hands-on 2: Report PPT Generation

**Page Area:** Chapter 05  
**HTML Reference:** `<section class="chapter-section" id="ch5">`  
**Visible Section:** “From dashboard deployment to executive PPT in one flow.”

Once the dashboard is created, the next step is reporting.

In business workflows, a dashboard alone is often not enough. Teams frequently need a PowerPoint version for executive reporting, monthly reviews, or team sharing.

The `pptx` skill helps convert dashboard insights into presentation material.

### 11-1. pptx Skill Concept

**Page Area:** Chapter 05 / 5-1  
**HTML Reference:** `#ch5` / `pptx Skill Concept`

The `pptx` skill can transform analysis and HTML-based outputs into PowerPoint format.

The important point is that the report should not simply be a screenshot. Wherever possible, charts should remain editable in PowerPoint.

If a company template is attached, Claude can be instructed to follow the master slide, fonts, and visual structure.

### 11-2. PPT Automation Practice

**Page Area:** Chapter 05 / 5-2  
**HTML Reference:** `#ch5` / `PPT Automation Practice`

A PowerPoint prompt should clearly define the report structure.

For example, include a cover page, executive summary, core metrics, channel-level analysis, and recommended next actions.

Also ask for editable native PowerPoint charts.

For China business reporting, Korean and Chinese fonts must render correctly. Font choices such as Noto Sans KR and Noto Sans SC should be considered to avoid missing-character boxes.

### 11-3. Deep Learning: Agent and Hook

**Page Area:** Chapter 05 / 5-3  
**HTML Reference:** `#ch5` / `Deep Learning - Build your own Agent and Hook`

This section introduces a more advanced automation concept.

An Agent can be understood as a role-based worker. For example, one Agent can validate the data, another can generate charts, and another can summarize insights for reporting.

A Hook is an automated procedure triggered at a specific moment. For example, when a data file is updated, a Hook can trigger a dashboard refresh or a quality check.

We will not fully automate everything today, but understanding this concept prepares us to reduce repetitive reporting work later.

---

## 12. DCS AI Internal Deployment

**Page Area:** Chapter 07  
**HTML Reference:** `<section class="chapter-section" id="ch7">`  
**Visible Section:** “Deploy internally through DCS AI.”

Finally, we will discuss how to share and deploy the output.

The dashboard and PowerPoint can be opened locally, but in real work they often need to be shared securely with the team.

DCS AI is F&F's internal AI infrastructure and tool environment. When connected to Claude Code through MCP, Claude can use approved internal resources to upload outputs and generate internal sharing links.

### 12-1. Dashboard Deployment Method

**Page Area:** Chapter 07 / 6-1  
**HTML Reference:** `#ch7` / `Dashboard Deployment - Where and how to share`

The sharing method depends on the situation.

Local HTML is useful for immediate personal review.

The internal intranet is appropriate for secure team sharing.

Messenger or email attachments are useful for smaller groups or quick distribution.

The key is to choose the deployment method based on who needs to access the output and how often it will be used.

### 12-2. What is DCS AI?

**Page Area:** Chapter 07 / 6-2  
**HTML Reference:** `#ch7` / `What is DCS AI?`

DCS AI is an internal AI infrastructure and tool environment that operates within an authenticated company environment.

Its key value is that outputs can be managed inside the company security boundary without relying on external services.

It can connect to internal tools such as Knowledge Graph APIs, artifact storage, skill catalogs, and S3 downloads.

In Claude Code, these tools can appear in the form of `dcsai__*`.

### 12-3. Connection Method

**Page Area:** Chapter 07 / 6-3  
**HTML Reference:** `#ch7` / `Connection Method - 3 Steps`

The connection process has three steps.

First, install the DCS AI plugin.

Second, complete internal authentication.

Third, confirm that the DCS AI tool list is visible in Claude Code.

If tools such as Knowledge Graph lookup, artifact upload, and skill catalog are visible, the connection is ready.

### 12-4. Deployment Prompt

**Page Area:** Chapter 07 / 6-4  
**HTML Reference:** `#ch7` / `Deployment Prompt Example`

Deployment can begin with a simple prompt.

For example, `please deploy dashboard` can instruct Claude to identify the current output and upload it to the DCS AI artifact repository.

If Plan Mode is on, Claude will show the deployment plan first and proceed only after approval.

After upload, DCS AI returns an internal sharing link. That link can be shared through internal messenger or email.

---

## 13. Session Closing

**Page Area:** Final CTA  
**HTML Reference:** `<section class="cta-light">`  
**Visible Section:** “Session Closing”

Let us close the session by summarizing the key points.

There are three main takeaways from today.

First, start with PLAN before asking AI to build.

Second, define the data, purpose, and reporting audience clearly.

Third, connect Claude Code Skills, pptx reporting, and DCS AI deployment into one practical workflow.

Today's output is based on sample data. However, the same structure can be applied to real business data and extended into a practical dashboard and reporting workflow.

The long-term goal is to move away from rebuilding reports from scratch. Instead, we want a repeatable structure where replacing the data can regenerate the dashboard and report.

I hope today's session helps you see Claude Code not just as a coding tool, but as a practical partner for business automation and reporting quality.

---

## 14. Footer and Resources

**Page Area:** Footer  
**HTML Reference:** `<footer>`  
**Visible Section:** Workshop links, scenario, resources, F&F links

At the bottom of the page, the key resources from today's session are organized for later reference.

You can jump back to Run-of-Show, Opening, PLAN, Skill Tour, Hands-on, and DCS AI deployment.

The Resources area can contain the workshop PDF, sample data, prompt templates, and output storage guide.

After the session, use this page together with your generated outputs as a reference for review and reuse.

For follow-up questions, please use the contact link at the bottom.
