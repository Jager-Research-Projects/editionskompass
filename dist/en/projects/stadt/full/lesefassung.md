# Die andere Stadt

## A novel in many versions. A project with four schedules.

Editorial test bench 0.4.2 · 2026-10-23

Die andere Stadt, Elise Hartmann and the edition team are fictitious. The examples are specially produced teaching material.

---

## The project

Elise Hartmann (1842–1901) worked on her novel *Die andere Stadt* between 1878 and 1886. In it the industrialization changes a city – and with it the life paths and relationships of its inhabitants. Hartmann began several times new, shifted chapters and let figures disappear. Individual chapters appeared in advance in magazines; the novel remained unfinished and was never published as a book.

The estate contains notebooks, two manuscript convolutes and a revised clean copy. Deletes, marginal additions and different leaf sequences tell different stories of its origin. Which designs belong together? What was changed when? Miriam Falk's team wants to make these relationships visible in a genetic edition and comprehensible on the digitalized manuscript. The printed volume offers a well-founded selected reading version and selected variations.

Lukas investigates the genesis of works; Nora traces how figures and narrative perspectives change. Both work on their own dissertations at the same time. Four years are funded, but research, publishing set and digital publication follow their own schedules.

**Leitfrage:** How does a common edition base remain reliable when research, publications and responsibilities run apart?

---

## What the Digital Frontend Unlocks

In which order were the sentences first placed? Where was a passage moved? Which supplement belongs to what writing phase? In the interface of the digital edition, reconstructions can be viewed side by side, individual layers can be displayed and directly compared with the manuscript page. The printed volume conveys selected variants and a well-founded reading sequence; changing arrangements and competing reconstructions can more easily be understood there. The scientifically responsible TEI data capture texts, variants and editorial relationships regardless of a single surface. They form the core of our digital edition and can feed different front ends, print editions and other research applications. The technical frontend provides an interface for the development of the digital Edition: its selection, comparison and image functions characterize what can be seen in the edition.

---

## Same words. Other reading sequence.

An edge note can be classified differently into the main text. Switch between two reconstructions and select a text part: its location on the demo page remains to be found.

### Reconstruction A

First Clara at the gate, then the darkening city: The marginal note is classified after Clara's arrival.

1. Clara stopped at the gate.
2. Behind the windows, the lamps were extinguished.
3. Only now did she hear the steps on the patch.

### Reconstruction B

First the darker city, then Clara at the gate: The same marginal note opens the passage. The connection is weighted differently.

1. Behind the windows, the lamps were extinguished.
2. Clara stopped at the gate.
3. Only now did she hear the steps on the patch.

The digital edition can reveal different reading sequences on the same material. The print chooses a well-founded sequence and explains alternatives in the apparatus.

**Git reference:** Git specifies which text parts, assignments and model rules are underlying a view. The historical order is an editorial hypothesis; it is not read from the sequence of modern commits.

---

## How we would proceed

1. The team starts on a small convoy. oXygen with Git client and a short joint process allow for independent corrections; the technology supports in conflicts.
2. The Editionsrepo is located in an institutional GitLab project group. Two designated persons can arrange administration and restoration.
3. A verified basic transcription is taken over in accordance with TEI. Afterwards, this unit is the relevant scientific working version in the Editionsrepo.
4. Edition data and frontend code are in separate repos. Versioned converters remain in the edition repo at first. Defined exports are in the import archive.
5. Lukas continues to develop a permanent alternative reconstruction on a designated research stand. Nora maintains additional figure relations in its own annotation repo.
6. Publications combine released data, schema, frontend and image references. Scientifically relevant typesetting corrections are returned to the TEI in a controlled manner.
7. In the past, research entries, local data copies, post-editing, institutional responsibility and restoration are regulated.

---

## Four schedules

- **funding:** The project sites and full infrastructure are secured for four years.The rate of funding remains available even if the project is completed later.
- **Dissertations:** Lukas started before the start of the project; Nora develops and announces its project after recruitment. The application plans to finalise the project; both research is expected to continue beyond that.
- **Book:** Completion in the application for the end of the project. Set costs are covered; later technical post-editing must be secured separately.
- **Edition frontend:** At the end of the project, the technical frontend should be available. Its interface allows you to read the digital edition, compare writing layers and connect text passages with the digitalized ones. The TEI data can also be published and used independently of it. For a later frontend start, the project, library and publishing house agree on a replacement route in advance: The publisher provides a simple reading view and the released TEI-version as download. Extent, version indication, update and responsibilities are recorded; genetic comparisons and image links of the planned interface are not yet fully available.

---

## We need to edit, not develop software

*Cooperation · P04-S01*

"We need your XML files in Git, says the technical team. Falk looks up from their records: "Why isn't our common folder enough?" Lukas knows Git about hearsay and thinks of conflicts. Nora prefers to ask: "What do I have to do for it every day?"

They try it in a single place. Nora corrects "Thore" to "Tore", compares the change and holds on to why it was necessary. Luke checks the picture. When Nora wants to see the old reading again, she is back immediately. "Good," she says. "But we write down the process.

**Note:** A good Git run makes the team independent and allows help to remain available.

### How we would proceed

Git captures changes and their relationships. A commit first secures in the local repo. Only transferring it to the project server makes it available there. The editorial check of the reading is a separate step.

**Example:** for example/lesung-vorher.xml → for example/ lieferstand-v1.xml: Thore becomes goal; the historical deletion and the margin addition are retained.

1. Set pilot convolute and simple daily routine.
2. Back up, transfer, compare and try editorial check together.
3. Establish a manual, introduction and technical representation.

** Done if:** A new employee can back up a TEI correction, transfer it to the project server and give it to the editorial check.

**How does Git help:** Git shows the changed position, the justification and the previous version. The institutional GitLab provides shared access.

### How we work together

The team agrees before the first access, which data may be used for edition work and dissertations, how contributions are assigned and who releases. Internal booths and Git history may not be passed on unauthorized. Local copies are protected; possible unauthorized access or device loss is immediately reported to the project management and the technical contact. The practical sequence of steps is in the versioned manual. The introduction includes an exercise in the oXygen-Git client.

**Opening terms:**

**Git and GitLab:** Git records file versions and its relationships. GitLab is the chosen platform for joint access, testing and project organization.

**Commit and Transfer:** A commit captures selected changes locally with a message. Transmitting makes these changes available on the project server.

**oXygen:** The XML editor supports TEI editing. A separate Git client add-on integrates comparison and version work; installation and access are part of the introduction.

---

## Exported again

*Import and data sovereignty · P04-S02*

The first handwriting unit is taken over in TEI. Lukas has distinguished a deleted formulation and the addition on the edge. Then comes a new export: An assistant in Transkribus has improved the reading "Thore". "Then we just take the new file?

Nora opens the comparison. The improved text is there. The genetic markup from her edition work is missing. They take over the reading purposefully. Export remains as proof of origin; the already edited TEI is continued.

**Note:** After the takeover, this edition file is processed in Git.

### How we would proceed

The transition takes place unit for unit: check basic transcription, fix export, document transformation, decrease import. This is not yet a publication release. Later corrections from Transkribus are compared as proposed changes; they do not replace an already enriched TEI file.

**Example:** example/renew-export.txt contains a better reading, but no genetic structure; lieferstand-v1.xml preserves the deletion and margin addition.

1. Document and secure the state of export and transformation.
2. Check text, border attachments, identifiers and image reference on import.
3. Introduce acceptance and subsequent correction rule into the manual.

** Done if:** For a unit origin, transfer, acceptance and relevant processing location are comprehensible.

**How Git helps:** Git makes visible which markup a new file version would lose. The controlled comparison allows a targeted takeover.

### Two decisions instead of one deadline

A document changes after passing the import check. The regular production phase of Transkribus ends only when the intended units have been passed and the inventory is correct. The goal is an early common TEI base. Difficult pages can be edited close to the image longer. For the pilot comparison we test PAGE XML with own versioned transformation against the available direct TEI export.

**Opening terms:**

**Transkribus, OCR and HTR:** The near-image environment supports detection and correction. OCR concerns printed, HTR handwritten texts. Export is checked prior to TEI further work.

**XML and TEI:** XML represents structured data. TEI provides a technical vocabulary for describing texts; the project determines its concrete use.

**Transformation:** A versioned procedure transfers an input structure to the required TEI. The result must be checked at the source material.

---

## The supplement is missing

*Digital Edition · P04-S03*

On the screen it says: "Clara stopped at the gate." Luke points to the edge of the manuscript view: "And where is the rest?" The TEI has long since added: "as if it didn't belong here." Nevertheless, the current view does not show it.

Nora and the developer check the same location. The viewer does not yet process the edge add-on. They complement display and test. In the published edition, the released version remains until the joint review of the previously released ZX Q0.

**Note:** Data, schema and representation must be checked together.

### How we would proceed

The genetic edition opens up changes and relationships to the manuscript. A reading version is a possible view. Also deletions, additions and their image references must remain comprehensible. We therefore check not only valid XML, but also whether the scientifically important information actually arrives.

**Example:** for example/lieferstand-v1.xml contains del and add. A test case must ensure that both are accessible in the genetic view.

1. Document a representative body and the expected views.
2. Test data rules, image anchor and display together.
3. Keep published data and code versions in the manifest.

** Done if:** The supplement is available in the intended view and the published combination of data, schema and frontend is specified.

**How Git helps:** Git versions data and code. approvals connect checked stands; unfinished changes do not automatically enter the public offer.

### Two stories of the same place

Hartmann stroked a formulation and added a part of the sentence on the edge. This belongs to the historical text genre. Nora corrects a reading today, Luke specifies the markup: this is part of the modern editing history in Git. The date of a commit does not date any historical writing work.

**Opening terms:**

**ODD and schema:** The project-specific TEI adjustment describes the model. A schema derived from it checks agreed structures; the interpretation is subject to technical examination.

**IIIF:** Common interfaces make use of images and their presentation structure. A canvas denotes a page or view; regions allow references to sections.

**Automatic tests:** Tests are repeated in case of changes. They detect, for example, faulty structures and references. A green test does not replace a test of the reading.

**Digital Genetic Edition:** The edition opens up designs, writing layers and relationships with digital means. Its scientific functions go beyond a mere online reading version.

---

# Show up early, release conscious.

Not everything has to wait until the end. The team can publish chapters, editing stages or individual functions earlier – if it plans scope, interests and approvals together.

## A conversation in the team

"Why wait with the front end until the whole novel is finished?" asks the developer. "We could already show index and Digitalisate. And try out a shared section together." Falk sees the advantage: Feedback comes at a time when the team can still react to it.

Lukas hesitates: "My new publication order has not yet been published." Nora nods. Also the publisher does not want to see the later volume completely anticipated. They therefore separate the questions: Which functions can already go online? Which texts and interpretations do they release when?

**Note:** Early partial publications need their own release plan – not the complete completion of the edition.

## Developing early – close to the edition

We start early and iteratively, but do the expansion according to the available material. A technical framework can be prepared from the start of the project. Technical views grow with a representative TEI pilot collection. Thus, the front end remains close to the respective edition stand instead of meeting a supposedly final inventory at the end.

In our case, the front end expansion follows with slight overlap on the actual edition work. This leaves little time for professional feedback before the sponsor. Falk therefore agrees at the beginning of the project an advanced technical preliminary and fixed development window with the chair's own IT. The existing capacity is re-planned; additional financial burdens are avoided. Tasks and time requirements are recorded in the updated work plan.

**Guideline:** Start: as early as possible, as late as necessary. Decrease core functions in time; then optimize as long as agreed capacity is available.

### 1 · Technical progress from project start

The technology prepares basic structure, data access, where appropriate the intended database connection and IIIF access. Test data checks interfaces and processes. Scientific cooperation is limited to the necessary basic decisions; developed test data do not determine edition hypotheses.

### 2 · Technical expansion with representative TEI

The pilot contains typical and difficult cases: edge addition, deletion, unclear assignment and stable image anchors. This limited model range is sufficiently described before the corresponding views are expanded. The entire TEI model does not have to be final yet. Modified rules get a versioned interface level and suitable tests.

### 3 · Short expansion and feedback windows

Technical editors and technicians check manageable views at the current edition stand. Feedback is bundled; not every everyday correction becomes a front-end discussion. The technology works in agreed windows instead of being bound continuously over the entire duration. Public approvals also follow the agreements with publishers and researchers.

### 4 · Core acceptance before end of funding, optimization afterwards within the agreed framework

The necessary core functions are removed with time for corrections. Further optimizations run as long as personnel and technical capacity are available. At an earlier necessary development end there is a viable, described version. Continuing development after job termination receives its own responsibility and capacity commitment.

### Consciously limit effort

**TEI remains in motion:** An immediate full expansion can create unnecessary modifications. Therefore, scientific views start with a viable model range and a real pilot stock; schema, data and code are tested together.

**Special work needs rest:** Permanent surface discussions draw energy from transcription and modeling. The team bundles requirements, designates a contact person and limits feedback to agreed dates.

**Development binds time:** Existing IT capacity must also be planned. Technical advance, expansion and subsequent corrections are given fixed windows. The goal is long improvement, not a permanent full-time commitment of the development team.

### Thus Git supports both development routes

We set up the same test basis. In the iterative way, it is often passed; in the phase model, it ensures the handovers and subsequent integration. Technical testing and technical rereading belong together.

### Iterative: small changes, often examine together

1. Create a short branch for a manageable task, e.g. for the display of marginal additions. The proposed change (merge request) contains expected behavior and the affected examples.
2. With every proposed change, the GitLab pipeline automatically checks: Do TEI and schema fit together? Do identifiers and image references remain intact? Can the frontend be built? Does the interface test show the edge addition in the right place? The technology generates a protected test view for the editors.
3. After successful examination and technical feedback, the change is taken over to the main level. In case of a model change, we also check the corresponding adjustment of the frontend. The integration protocol determines which data, schema and code commits have been tested together.

**Example:** Nora reports: The edge add-on is missing in the interface. The amendment proposal complements view and test case. After that, Nora checks exactly this point in the test view; the pipeline also checks the previous sample cases.

### In phases: making handovers clear and repeatable

1. Already during the edition phase, editors and technology agree on the transfer format. schema, representative TEI examples and expected editions are available versioned. Automatic checks report deviations even if the actual frontend expansion starts later.
2. At the end of the phase, we mark the taken delivery stand with an annotated tag, e.g. tei-uegabe-01. The handover log also specifies the exact commit, the schema and known open points. The development explicitly refers to this version, not continuously the latest working version.
3. The first integration run builds the front end against this basis and checks the agreed example cases. Corrections are made as short suggestions for changes to the relevant data. A new transfer position replaces the old one only after a new joint examination; we do not postpone the old day.

**Example:** The editor provides TEI-version 01. While the technique works with it, an image reference is corrected. The correction gets its own amendment proposal and then a new transfer state. Thus, it can be seen which version the development actually uses.

### Hooks: check early at work

A pre-commit hook checks the scheduled XML files before saving a commit and reports invalid markup or double identifiers. The technique holds hook and test scripts in the repo, sets them up during onboarding and documents the required tools. Local hooks must be activated on each workstation and can be bypassed. Therefore, the central pipeline repeats the mandatory tests.

### Pipeline: Secure the common version

The pipeline is a test run set up on the GitLab server, not a built-in XML tester from Git. We version their configuration and use defined tool versions. Automatic tests also check the combination of the intended data, schema and code sets from the separate repos. The main branch is protected; takeovers require successful statutory checks and agreed review. Test reports and test view remain in the authorized team. A green test does not replace editorial acceptance.

### Mark, repeat, selectively withdraw

We record the exact data, schema and code-commits as well as construction instructions and tool versions for each accepted integration level. Tags make such milestones easy to find. Test results and test views are backed up accordingly; short-lived pipeline artifacts are not a permanent archive. If a change causes an error, git revert can take them back by means of a new, comprehensible commit. Subsequently, the combination is checked again. Separate repos are expressly coordinated.

**The first specific task:** The technology initially sets up a versioned test call for local hooks and pipelines. The editors provide typical and difficult sample sites together with an expected presentation. Together they test a valid and deliberately faulty test stand as well as the re-assembly of a designated integration level.

**Completed if:** An amendment proposal with faulty test material is reliably stopped; a permissible version can be rebuilt and tested using its data and code identifiers.

Technical basics: [Git: Hooks](https://git-scm.com/docs/githooks) · [GitLab: CI/CD pipelines] (https://docs.gitlab.com/ci/pipelines/)

## Three ways to combine

### Functions first

index, digitalisats view or full text search can be used before the edited texts are completely available.

**Example:** A released index opens up manuscript pages. The search initially works on a designated transcription stock and leads to the digitalisat.

**Git strategy:** Frontend code, search index, index and data base receive separate version references. The public combination is released as tested integration status.

**Before the approval:** Also index, search index, hit texts and picture entries belong in the ZX Q2. Not yet published interpretation is not visible unchecked.

### Publish chapter by chapter

An audited subset will be published as a designated sub-issue and further chapters will be added later.

**Example:** A first chapter with its draft versions appears, while other volumes are still being edited.

**Git strategy:** Each release lists the contained units and their model/test stands. The output remains citable, even if further chapters follow.

**Before the approval:** With publishers and researchers text scope, variants, comments and date are agreed. Missing chapters are made visible in the table of contents.

### Show editing steps

First, a tested basic transcription will be published; genetic distinction and comments will follow in new versions.

**Example:** Version 0.1 offers a tested transcription. Version 0.2 supplements a first designated annotation layer; later follows the fully responsible genetic representation.

**Git strategy:** Transcription, annotation and editorial approval are documented per unit. New versions do not tacitly replace the cited older edition.

**Before the approval:** A transcription is called a transcription, not a finished genetic edition. Additional annotations are given their own version and test status.

## Publishing and Dissertation

The publishing house wants to see the printed book completely anticipated not long before its publication. Lukas and Nora want to determine the timing and form of their own research publications. Therefore, the team determines for each partial edition which texts, index, search hits, comments and interpretations become public. Internal testing can start earlier: Tests and feedback are also possible with a limited access. The agreed public parts then go online purposefully.

## Alternative scenario: cumulative dissertations

In an alternative scenario, Lukas and Nora agree on a cumulative doctorate: Associated scientific contributions arise and appear during the research work. An early, clearly responsible publication can then lie in their own interest. Lukas could justify his new reconstruction in an independent contribution; Nora could combine her figure analysis with a published annotation version. Both can refer to the appropriate edition of the web edition. Which forms of publication, review and own parts count, is clarified early with supervision and responsible faculty according to the current doctoral regulations. This may reduce the print to have to hold everything back until a single final publication.

## Cite and allocate contributions

For a concrete analysis, an archived edition with version DOI is quoted; job identifiers refer to the examined passage. On the website there are authorship and responsibility shares for the respective contribution. The further developed edition links the older version and the contribution. A DOI makes the version referenceable; the recognition as a doctoral achievement depends on the agreed technical and formal requirements.

## That's how we would start

We develop the frontend early and iterative. Basic frameworks and interface tests can be developed at the beginning of the project; the technical development starts with representative TEI data. In agreed feedback windows, we keep the digital views close to the respective edition level. Core functions are taken off in good time before the end of the project and optimize further as long as capacity is available. A released public function can be used early; chapters and editing steps follow according to the agreed approvals. For operation and maintenance a contact is named. The sentence lies with the publisher; own early sentence previews are not part of the project process in this model.

1. agree technical progress and development window in the work plan; define a representative TEI pilot stock and a limited model range.
2. Test views at the current edition state; bundle feedback and coordinate public approvals with publisher and doctoral researchers.
3. Decrease core functions with test buffer; document further partial releases, archive references, optimizations and available connection capacity.

** Done if:** A first agreed offer is publicly usable, its scope and data level are recognisable, feedback has a responsible recipient and the next issue has a concrete task.

## Background and sources

- [Kumulative Dissertation · Faculty of Arts and Humanities Göttingen](https://www.uni-goettingen.de/de/689605.html): Ein Beispiel auch für Neuere deutsche Literatur und Digital Humanities. Die Anforderungen entscheiden Publikationsfähigkeit und individuelle Beiträge; bestimmlich ist die jegenden Promotionordnung.

- [Zenodo · DOI Versionation](https://zenodo.org/help/versioning): Versions DOIs refer to a specific output; an overarching DOI can represent all versions.


---

## Luke reorders a sheet

*In-house research · P04-S04*

Lukas puts two leaf copies side by side. "I think our order isn't right here." A finding of the foliar sequence suggests that Clara's passage was created later than previously assumed. Of all things, his own early reconstruction is now under discussion.

Nora listens attentively. Her dissertation traces when Clara disappears from the novel. "Then this changes my interpretation as well. They examine the findings together. Lukas develops the alternative order first in his own research inventory; Nora records on which edition version their character relations are based.

**Note:** Independent research needs a designated starting point and space for other interpretations.

### How we would proceed

A short branch is suitable for a limited change, which should come back to the examination. A long-term different reconstruction receives its own research repo. Nora complements her character relations separately as version-off annotation: The references refer to stable positions and a concrete edition status. The editorial department decides on a change of the official edition after scientific discussion.

**Example:** for example/forschungsbezug.json separates Lukas and Nora's alternative leaf order from additional character relation.

1. Name initial release, stable identifiers and research question.
2. Choose work form: short branch, standalone inventory or additional annotation.
3. Technically examine and document acquisitions and changed references.

** Done if:** Both dissertations can reproduce their data reference; the official edition will not be remodelled unnoticed.

**How Git helps:** Git preserves alternative processes and enables targeted comparisons and acquisitions. Scientific validity is assessed professionally.

### Fork, Branch and Permission

A branch is a parallel course within a repos. A fork is a branch linked on the platform in a separate project; visibility and access depend on the platform rules. Before the fork these are checked. For permanently own confidential research, a separately set up repo can be more suitable. A branch does not protect private dissertation parts from other persons with corresponding repo access.

**Opening terms:**

**Branch:** A parallel processing process in the same repo, for example for a limited change with later testing.

**Fork:** A branching off of a repos on the platform in a separate project. Rules for visibility and access must fit the intended use.

**version-off annotation:** Additional markup is saved separately and refers to precisely designated places in a basic version.

---

## It's already corrected in the book

*publications · P04-S05*

The flag still says "as if it didn't belong here." When looking back at the manuscript, Nora realizes: "there is a better reading there. The sentence is corrected. "Is that already in our data?" Falk asks. Not yet.

The team returns the correction to the TEI and releases V2. The book remains in typesetting; the library is not yet able to provide the planned edition frontend. As a substitute, the project and publisher have agreed on a simple read view with TEI download. The publisher prepares this offer. For TEI download they expressly agree V2.

**Note:** Book, TEI and web offer need comprehensible version relationships.

### How we would proceed

The editors examine technical typesetting corrections and incorporate them into the edition data. Typographic adjustments are treated separately. A tag marks the released Git-version; a release describes and bundles it. The archive version receives its own metadata. The reduced publisher view provides access, but does not offer all the genetic comparison and image functions of the planned edition frontend.

**Example:** example/lieferstand-v1.xml → referenzstand-v2.xml: here becomes to there. The typesetting correction is indicated in the correction protocol.

1. Repayment of corrections and responsible post-editing before the end of funding.
2. Apply and examine scientificly relevant typesetting corrections.
3. Mark book reference, TEI download and web combination with actual versions.

** Done if:** V2 contains the correction; download and publication description indicate the correct version. Responsibility for subsequent changes is agreed.

**How does Git:** Git documents the return. Named booths and a manifesto combine delivery version, correction and output.

### When the download first lags behind

If the publisher first has to offer V1, it will be published as a set entry state with named correction status. Subsequent V2 will receive a new designation and an amendment notice. No existing version will be issued tacitly as identical to the finished book. The public viewer will only be changed to V2 after his own test. The sentence funds remain secured. However, the expiring project posts do not automatically finance further scientific post-editing.

**Opening terms:**

**Tag:** A named marking of a Git stand. A marking alone does not perform an inspection and does not secure independent archiving.

**Release:** A described edition, which the team releases according to its rules. Data, test result and release notes belong together.

**Archived version:** A described received package with responsibility and, if necessary, persistent identifier; regardless of the ongoing processing.

---

## The thesis does not end.

*Continued work · P04-S06*

Nora puts her desk together. There is another task waiting for her at the new university; she takes her dissertation with her. "And the figure annotation?" Lukas asks. "That too," she says. "But we prefer to test the access now."

They jointly check which data Nora is allowed to use and which copies it owns. The library takes over a described archive package. Falk and the designated editors remain responsible for post-corrections at the edition. The technical contact shows his representative how an audited version is restored.

**Note:** Further work is prepared and practically tested before the end of the job.

### How we would proceed

The new role is documented: own research access, official write rights, approval and administration are different powers. The agreement regulates permitted copies, protection, return or deletion as well as justified exceptions and the subsequent associated cooperation. The same role check applies to external technology, publishing house and library; their agreements depend on task and access.

**Example:** example/zugangsmatrix.json distinguishes core team, associated research, technical support and receiving facilities.

1. Check the research stock, rights of use and functioning access before the end of the job.
2. Separately assign technical post-editing, administration, image operation and archive.
3. Test recovery and a limited post-correction by a second person.

**Completed if:** Nora can use their agreed state of research. A second qualified person can restore and check the documented state of the edition.

**How Git helps:** A git clone or bundle can transfer the data history. Platform functions, permissions and external image services are additionally secured or re-installed.

### What a host change additionally requires

In addition to files and Git history, open tasks, verification configuration, protected approvals, accesses and references are controlled. Secrets and access keys are managed separately securely. An archive announcement does not include an automatic commitment for front-end operation or scientific post-editing.

**Opening terms:**

**Migration:** A controlled move of data and processes. Git history and additional platform functions are checked separately.

**Responsibility and administration:** Technical approval, server management, rights to data and operation are different tasks. They are assigned to persons or institutions.

---

## Related materials

- [Model strategy](musterstrategie.md)
- [Order, Manual and Agreements](handbuch.md)
- [Demost](assets/demostelle.zip)
- [Sources and test limits](quellen.md)
