# Git Antipattern Academy — English learning catalogue

Translation of the supplied conceptual catalogue dated 19 October 2026. The German source is included separately. Scenarios illustrating exceptions are editorial additions.

A smell is a clue, not proof. Working and publication repositories describe functions, not necessarily two separate technical repositories. This is a conceptual typology, not an empirical frequency study. Legal questions require assessment under the applicable law.

## A1. The version in the filename

**Context:** Working and publication environments.

**Problem:** Versions of a file must be preserved and distinguished.

**Adopted practice:** Save every version as a separate file with version numbers, dates and names in the filename.

**Appeal:** Simple, immediately understandable, and requires no special infrastructure.

**Consequences:** The sequence and authoritative version become unclear; changes are not systematically documented, and naming conventions break down during parallel work.

**Alternative:** Use version control with stable filenames; identify defined exports with clear version identifiers.

**Rationale:** Filenames take over the management of versions and their relationships from a suitable system.

**Smells:** Files such as final_new.xml and final_v3_corrected.xml compete for authority.

**Scope and exceptions:** Version identifiers in immutable publication exports are legitimate. Using file copies as the sole means of working version control is problematic.

**Example of a legitimate context:** Immutable publication exports have version identifiers in their filenames; ongoing work is also managed with version control.

## A2. The copy zoo

**Context:** Primarily the working environment.

**Problem:** Files need protection against loss and must be available to several people.

**Adopted practice:** Exchange independently edited folder copies informally across computers, drives and storage devices.

**Appeal:** Familiar routines, offline work and an apparent increase in safety.

**Consequences:** Competing versions, missed changes, overwriting and laborious reconciliation result.

**Alternative:** Use coordinated synchronisation with version control and independent backups.

**Rationale:** Uncoordinated replication does not solve collaborative editing.

**Smells:** Edition_backup, Edition_new and Edition_Anna each contain different supposedly current files.

**Scope and exceptions:** Controlled backups, archival snapshots and explicitly immutable exports are useful.

**Example of a legitimate context:** A project creates controlled, immutable backup copies and reconciles working versions through a defined process.

## A3. History without a past

**Context:** Both functions; especially important for reconstructing editorial work.

**Problem:** Edition data need improvement and publication.

**Adopted practice:** Overwrite earlier working versions or discard them after publication.

**Appeal:** Less storage and organisational effort; focus on the final product.

**Consequences:** Decisions, corrections and rejected readings can no longer be reconstructed.

**Alternative:** Use version control and a deliberate preservation strategy, reviewed for legal requirements, for scientifically relevant process documentation.

**Rationale:** Keeping only results may destroy necessary historical information.

**Smells:** Only the published final version remains; earlier readings cannot be reconstructed.

**Scope and exceptions:** Not every transient draft warrants archiving. A publication repository need not contain the entire internal working history.

**Example of a legitimate context:** A publication repository contains only reviewed final versions; relevant process documentation is preserved separately under an assessed preservation strategy.

## D3. Git is our backup

**Context:** Both functions.

**Problem:** Data loss and corruption must be prevented.

**Adopted practice:** Let the existing Git repository replace all independent backup procedures.

**Appeal:** Git retains versions and is often copied onto several computers.

**Consequences:** Unpushed work, lost credentials or failure of all accessible copies may remain unprotected.

**Alternative:** Document and test a backup and recovery strategy in which Git can be one component.

**Rationale:** Version control and full disaster recovery meet different requirements.

**Smells:** “We have GitHub, so we do not need backups”; no restore tests.

**Scope and exceptions:** Git can form a substantial part of a robust backup strategy.

**Example of a legitimate context:** Git is one part of a documented backup strategy with independent copies and tested recovery.

## D4. The ownerless repository

**Context:** Both functions.

**Problem:** Long-term infrastructure needs technical operation and scholarly responsibility.

**Adopted practice:** Leave administration, rights clearance and decisions informally with individuals, without substitution or handover arrangements.

**Appeal:** Direct communication and little formalisation.

**Consequences:** Access may be lost, succession may fail, and publication and security decisions remain unclear.

**Alternative:** Document institutional, scholarly, technical and data-protection responsibilities, including deputies and handover procedures.

**Rationale:** Essential long-term infrastructure depends on unsecured personal availability.

**Smells:** A private account is the sole owner; nobody knows what happens when the administrator leaves.

**Scope and exceptions:** Individuals may be responsible, but responsibility must be transferable and appropriately secured.

**Example of a legitimate context:** One person administers the repository; deputies, institutional responsibility and handover procedures are defined.

## B1. Metadata on the move

**Context:** Both functions; especially critical for publication.

**Problem:** Scholarly properties, editing status and responsibilities need documentation and querying.

**Adopted practice:** Keep them exclusively in commit messages, tags, branches, issues, filenames or folders instead of suitable structured metadata.

**Appeal:** The Git environment already exists and seems to avoid duplicate maintenance.

**Consequences:** Information is scattered, inconsistently modelled and may be lost when edition data are distributed separately.

**Alternative:** Use TEI headers where appropriate, such as revisionDesc, scholarly metadata files or another suitable structured model; add Git references as a supplement.

**Rationale:** Technical work organisation replaces necessary scholarly information modelling.

**Smells:** Commit messages record review status while scholarly status fields remain empty; /finished/ is the only status source.

**Scope and exceptions:** Provisional or redundant Git information is legitimate. The problem arises when necessary long-term scholarly information remains exclusively there.

**Example of a legitimate context:** Review status is also recorded in a commit; the long-term scholarly status is maintained in structured metadata as well.

## B2. The branch as an edition model

**Context:** Both functions.

**Problem:** Diplomatic, normalised or other scholarly versions need to be maintained in parallel.

**Adopted practice:** Represent their scholarly identity and relationships exclusively through branches.

**Appeal:** Git directly supports parallel development branches.

**Consequences:** Relationships remain implicit; a moving branch name is not a stable scholarly version.

**Alternative:** Model scholarly representations and relationships explicitly, using transformations where appropriate; develop in branches and use defined releases for citable versions.

**Rationale:** A technical development mechanism replaces edition theory and the data model.

**Smells:** Only branches named diplomatic and normalised identify versions; no explanation exists outside the branch structure.

**Scope and exceptions:** Even long-lived version branches can be appropriate if their scholarly meaning is explicitly documented.

**Example of a legitimate context:** Long-lived version branches are used; the scholarly versions and their relationships are explicitly documented outside the branch structure.

## B3. The hidden editorial decision

**Context:** Both functions.

**Problem:** Text-critical decisions need justification and traceability.

**Adopted practice:** Keep the only justification in commit messages, issues or pull-request discussions.

**Appeal:** Discussion and implementation remain closely connected.

**Consequences:** Readers and exported editions lose access to the justification; scholarly decisions depend on the working platform.

**Alternative:** Move publication-relevant justifications into the apparatus, commentary or edition documentation; link Git discussions as supplementary material.

**Rationale:** Technical communication replaces the scholarly presentation of a decision.

**Smells:** “Reading B instead of A because of manuscript X” appears only in a commit.

**Scope and exceptions:** Not every working discussion needs publication; the necessary justification of the published edition matters.

**Example of a legitimate context:** A working discussion stays in an issue; the publication-relevant justification is transferred to the edition commentary.

## B4. The orphaned editorial status

**Context:** Transition from working to publication function.

**Problem:** A working version must be assessed for publication readiness.

**Adopted practice:** Automatically treat an operational status such as a closed issue, merged branch or done column as scholarly approval.

**Appeal:** A simple workflow without duplicate status tracking.

**Consequences:** Approval criteria remain implicit, and incomplete or unchecked data may be published.

**Alternative:** Define an explicit, traceable approval process with stated checks and a documented result.

**Rationale:** Work organisation is equated with scholarly quality assessment without justification.

**Smells:** A merge automatically means edited and reviewed; separate approval criteria are absent.

**Scope and exceptions:** A project board can represent approval if the status is tied to verifiable criteria and responsibilities.

**Example of a legitimate context:** Board status represents scholarly approval and is tied to verifiable criteria and named responsibilities.

## C5. The unchecked publication

**Context:** Publication repository.

**Problem:** New editorial results should become available quickly.

**Adopted practice:** Publish new working versions directly without defined quality checks.

**Appeal:** Fast publication that is easy to automate.

**Consequences:** Invalid, inconsistent or unfinished data acquire published status.

**Alternative:** Use validation, project-specific tests and explicit publication approval.

**Rationale:** A technical commit or merge replaces a quality decision.

**Smells:** Every push to main publishes unchecked TEI files; known validation errors are public.

**Scope and exceptions:** Public experimental working versions may be unfinished if clearly labelled. Direct commits to main are not the problem in themselves.

**Example of a legitimate context:** Unfinished working versions are publicly labelled experimental and are not presented as approved publications.

## G1. The unspoken Git agreement

**Context:** Both functions.

**Problem:** Collaboration should start without extensive preliminary organisation.

**Adopted practice:** Treat repository access as implicit agreement on rights, duties and future uses of working data.

**Appeal:** An informal, familiar project culture with little bureaucracy.

**Consequences:** Conflicts arise over access, publication, credit and permissible data use.

**Alternative:** Provide binding, understandable repository rules, supplemented by legally required agreements and information.

**Rationale:** Informal participation does not replace effective rules for relevant rights and protective interests.

**Smells:** There is no repository policy; rights questions are answered with “we always do it this way”.

**Scope and exceptions:** Existing institutional rules may suffice; not every issue requires a separate individual contract.

**Example of a legitimate context:** Understandable institutional rules already clarify the relevant rights and duties; an additional individual contract is unnecessary for those matters.

## D1. Access forever

**Context:** Both functions; particularly read access in private working repositories and write/admin access in publication repositories.

**Problem:** Contributors need access rights for their tasks.

**Adopted practice:** Grant permissions on entry but never review or revoke them when tasks change or people leave.

**Appeal:** Little ongoing administration and easy possible future collaboration.

**Consequences:** Unnecessary access or editing powers, unclear accountability and increased misuse or error risks remain.

**Alternative:** Assign only role-appropriate necessary rights, review them regularly and define onboarding and offboarding, including service accounts.

**Rationale:** An original authorisation continues unchanged after its purpose disappears.

**Smells:** Former contributors retain write or administrator access; access lists are never reviewed.

**Scope and exceptions:** Ongoing work can justify explicitly renewed permissions. Revocation does not prevent use of copies already made.

**Example of a legitimate context:** A former staff member continues in a defined role; their permission is reviewed and explicitly renewed with a justification.

## G4. The unclear chain of rights

**Context:** Both functions.

**Problem:** Collaborative research data need editing, publication, licensing and archiving.

**Adopted practice:** Treat the ability to commit contributions as sufficient permission for all later uses.

**Appeal:** Work proceeds without delays for rights clearance.

**Consequences:** Permitted editing, distribution, licensing and archiving of individual components remain unclear.

**Alternative:** Clarify and document protection status, rights holders and required permissions for different contribution types early.

**Rationale:** Technical access rights are confused with copyright and usage permissions.

**Smells:** No rights inventory covers commentary, translations, digitised images and software; licences are assigned without known rights status.

**Scope and exceptions:** Not every contribution is protected by copyright; contracts or other rules may already settle rights. Applicable law matters.

**Example of a legitimate context:** Protection status, rights holders and the required usage permissions for a contribution have been clarified and documented.

## G5. Licensing at the click of a button

**Context:** Publication repository.

**Problem:** An edition should be as openly reusable as possible.

**Adopted practice:** Apply a single licence indiscriminately to TEI, scholarly texts, software, translations and third-party material.

**Appeal:** Quick and seemingly clear open-science labelling.

**Consequences:** Misleading rights promises and potentially unauthorised licensing of third-party resources result.

**Alternative:** Provide clear resource-specific rights and licensing information; use a single licence only where rights are genuinely uniform.

**Rationale:** A single technical notice purports to override different usage rights.

**Smells:** One LICENSE supposedly covers external digitised images and original software alike without differentiation.

**Scope and exceptions:** A uniform licence is useful if it effectively covers every relevant resource.

**Example of a legitimate context:** A single licence is used after establishing that it effectively covers all relevant resources.

## G2. Blanket consent

**Context:** Primarily the working repository.

**Problem:** Personal Git data are to be used for different purposes.

**Adopted practice:** Treat a broad initial declaration as permission for all current and future analyses and publications.

**Appeal:** An apparently simple one-off safeguard.

**Consequences:** Purposes and scope remain unclear; consent may be invalid, especially in dependent employment relationships.

**Alternative:** Clarify purposes, suitable legal bases, information and safeguards for each use; obtain valid specific consent where appropriate.

**Rationale:** Blanket agreement replaces necessary legal and organisational assessment.

**Smells:** “By participating, you consent to all future analyses and publication of all Git data.”

**Scope and exceptions:** Voluntary, informed and sufficiently specific consent can be legitimate in suitable circumstances; it is not the only possible legal basis.

**Example of a legitimate context:** Voluntary, informed and sufficiently specific consent is obtained for a defined use in a suitable context.

## E1. The commit as proof of performance

**Context:** Primarily the working repository.

**Problem:** Progress and individual performance need assessment.

**Adopted practice:** Interpret commit counts, changed lines and frequency directly as performance or productivity.

**Appeal:** Readily available quantitative indicators seem objective.

**Consequences:** Comparisons are distorted, incentives become misleading and different activities are judged unfairly.

**Alternative:** Use scholarly, contextual criteria and qualitative assessment, including work not recorded in Git.

**Rationale:** Technical activity does not directly measure scholarly quality or performance.

**Smells:** Staff rankings by commit count; lines added is used as a progress measure.

**Scope and exceptions:** These numbers can be useful as descriptive project metrics. Permission for processing personal data is a separate question addressed by G3.

**Example of a legitimate context:** Commit counts are used as descriptive project metrics with explicit limits; personal data processing has been assessed separately.

## E2. Git as an all-knowing witness

**Context:** Primarily the working repository.

**Problem:** The editorial process needs reconstruction.

**Adopted practice:** Treat Git history as a complete record of scholarly work and decision-making.

**Appeal:** Detailed, chronologically ordered technical records include author and change information.

**Consequences:** Offline work, instructions, discussions and collaborative authorship are overlooked.

**Alternative:** Use Git as a limited source alongside other process sources and contextual knowledge.

**Rationale:** A selective technical record is mistaken for the whole scholarly process.

**Smells:** “Git shows everything”; missing commits mean no work; the commit author is automatically treated as the responsible scholar.

**Scope and exceptions:** Claims about Git activity itself are possible when their scope is stated accurately.

**Example of a legitimate context:** An investigation describes observed Git activity only and makes no claim to capture the entire editorial process.

## G3. Purpose drift in Git data

**Context:** Working repository.

**Problem:** Project management wants to understand workflows and bottlenecks.

**Adopted practice:** Reuse personal version-control data for attendance monitoring, individual performance assessment or personnel decisions without a separate assessment.

**Appeal:** The data already exist and can be visualised automatically.

**Consequences:** Purpose drift, loss of trust, possible infringements of employee rights and misinterpretation result.

**Alternative:** Assess each analysis purpose and legal basis; use suitable access restrictions, data minimisation and aggregated analysis where appropriate.

**Rationale:** A technical dataset is reused for new personal purposes without sufficient justification.

**Smells:** Commit heatmaps appear in performance meetings; Git logs become timesheets without previously established rules.

**Scope and exceptions:** Project-related analyses can be legitimate. This is separate from whether the resulting metric is methodologically sound, addressed by E1.

**Example of a legitimate context:** A project-related analysis takes place only after its purpose, legal basis and appropriate safeguards have been assessed.

## G6. The unlimited working chronicle

**Context:** Primarily the working repository and its archiving.

**Problem:** The editorial process should be preserved long-term as a research source.

**Adopted practice:** Keep complete personal Git histories indefinitely without defined purposes, retention periods, access rules or safeguards.

**Appeal:** Maximum completeness without prematurely destroying potentially relevant process data.

**Consequences:** Personal work profiles and internal communications remain reconstructable long-term without an adequate protective framework.

**Alternative:** Define a justified retention and archiving policy with differentiated access, safeguards and consideration of scholarly and personal interests.

**Rationale:** Technical storage capability is confused with permission for unlimited retention.

**Smells:** “Archive everything forever” without rules; historical personal data remain accessible indefinitely.

**Scope and exceptions:** Long-term scholarly archiving can be lawful and useful but needs suitable legal and organisational conditions.

**Example of a legitimate context:** Scholarly process data are retained under a justified archiving policy with appropriate access rules and safeguards.

## D2. The forgotten Git past

**Context:** Especially when making a publication repository public.

**Problem:** Confidential data must be removed before publication.

**Adopted practice:** Clean only the current data while publishing the earlier Git history unchanged.

**Appeal:** The visible current XML looks clean; history is not seen as a separate dataset.

**Consequences:** Earlier XML comments, personal information or secrets remain recoverable.

**Alternative:** Review the entire dataset to be released, including history; consider a separate publication repository.

**Rationale:** Removal from HEAD is mistaken for complete deletion.

**Smells:** Earlier commits contain internal XML comments; formerly private working history becomes public unchanged.

**Scope and exceptions:** Permissible internal preservation may be useful. Rewriting history alone does not reliably remove copies already distributed.

**Example of a legitimate context:** A permissible internal history remains protected; the entire dataset intended for publication is reviewed separately.

## C1. The tangled commit

**Context:** Primarily the working repository.

**Problem:** Many changes need to be versioned.

**Adopted practice:** Bundle unrelated changes into one commit without a recognisable common unit.

**Appeal:** Quick commits after long working sessions.

**Consequences:** Changes are difficult to review, explain and selectively revert.

**Alternative:** Group logically related changes; document separate bulk operations.

**Rationale:** Lack of scholarly coherence, rather than size, undermines the history.

**Smells:** “Updated everything” changes transcription, commentary, software and configuration without a common purpose.

**Scope and exceptions:** A large coherent data import is legitimate and particularly common in publication repositories.

**Example of a legitimate context:** A large data import is committed as a coherent, documented unit.

## C2. The uninformative history

**Context:** Primarily the working repository.

**Problem:** Changes should be recorded without delay.

**Adopted practice:** Use messages that give insufficient indication of a commit’s subject or purpose.

**Appeal:** A low entry barrier; the actual changes are visible in the diff.

**Consequences:** Searching, understanding and later reconstruction take more effort.

**Alternative:** Write brief, informative messages following an understandable convention.

**Rationale:** A documentation feature is devalued without a corresponding benefit.

**Smells:** Repeated fix, asdf, again and update messages for complex changes.

**Scope and exceptions:** Short or automatically generated messages are not inherently problematic if their purpose is clear enough.

**Example of a legitimate context:** A brief automatically generated commit message makes the subject and purpose of the change sufficiently clear.

## C3. Integration postponed

**Context:** Working repository.

**Problem:** Contributors should be able to work independently.

**Adopted practice:** Keep shared changes in separate branches for a long time and reconcile them only late.

**Appeal:** Few short-term conflicts and maximum autonomy.

**Consequences:** Divergence, integration effort and late discovery of contradictions increase.

**Alternative:** Reconcile and integrate regularly according to the actual dependencies between work packages.

**Rationale:** Coordination avoided now is deferred and may grow.

**Smells:** anna and mark diverge from main for years; merges are avoided because of conflicts.

**Scope and exceptions:** Long-lived separate branches are legitimate if tasks are independent or separation is deliberately justified.

**Example of a legitimate context:** Long-lived separate branches address independent tasks; the separation is deliberately justified.

## C4. The formatting tsunami

**Context:** Primarily the working repository.

**Problem:** XML needs readable, consistent formatting.

**Adopted practice:** Let editors reformat indentation, whitespace or line breaks extensively during small scholarly edits.

**Appeal:** Local readability and automatic standardisation.

**Consequences:** Relevant diffs are obscured, blame becomes less informative and conflicts increase.

**Alternative:** Use stable shared editor and formatting conventions; commit formatting-only changes separately.

**Rationale:** Non-content changes undermine a central documentation function of the working repository.

**Smells:** A one-word correction produces hundreds of changed lines.

**Scope and exceptions:** Deliberate formatting migrations are legitimate; detailed line history may matter less in a publication repository.

**Example of a legitimate context:** A deliberate formatting migration is announced, checked and committed separately from scholarly changes.

## C6. The moving publication

**Context:** Publication repository.

**Problem:** A continuously updated edition also needs to be citable.

**Adopted practice:** Identify only the moving tip of a branch such as main as the published version.

**Appeal:** One current URL and no extra release effort.

**Consequences:** Previously cited versions become hard to identify and reproducibility suffers.

**Alternative:** Provide immutable, clearly identified releases and persistent identifiers where suitable, alongside latest access.

**Rationale:** A moving reference exclusively takes the place of a stable publication version.

**Smells:** Publications link only to /tree/main; documented versions are absent.

**Scope and exceptions:** An always-current version is useful if earlier publication versions remain unambiguously referenceable.

**Example of a legitimate context:** A current latest version is offered; earlier publications remain referenceable as immutable, clearly identified releases.
