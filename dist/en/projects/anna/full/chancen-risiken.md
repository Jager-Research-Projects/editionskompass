# Anna: Opportunities and Risks – Detailed Editorial

version: October 20, 2026 · Prototype 0.3 / Grammar 0.5.0

Basic condition, qualitative assessments for five years. Condition-dependent changes are supplemented in the web view.

## Support

ID: P01-C01

**Medium / medium**

It would be very gratifying if Anna found fellow contenders for her project – perhaps someone who reads the commentary carefully. Four eyes see more than two! Mira could know a parallel point, discover someone else's mistakes in the references. Matching expertise is conceivable; before a concrete commitment, participation and professional gain remain open.

**How does Git help?** Anna can invite more people via the hosting service and track changes. Mira can read a section and send hints or propose changes with appropriate access. A pull/merge request bundles a proposal together with discussion; Anna can have it reviewed, and specifically take over. The available roles depend on the respective service.

**What is there to consider?** Should all participants be able to read all work data including achievable history? A separate editing branch does not hide any files. For a limited order, an adjusted section can suffice. Reading or writing? Notes by mail, as issue or as proposed changes? Who decides on the takeover? Technical contributions are appreciated according to agreed rules, for example in the TEI header (respStmt) and change directory (revisionDesc/change). Commitmetadata help with the assignment, but do not replace this attribute and the explanation of responsibility.

**Action:** Set up access suitable for contributors, initially reading only if necessary. Arrange an understandable review section, feedback channel, integration responsibility and form of recognition.

**Responsible:** Anna and possible contributors

[TEI: Responsibilities](https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-respStmt.html) · [ZXq2: Change Directory] (https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-revisionDesc.html)

## Revision

ID: P01-C02

**Medium / high**

One year after the release, Anna discovers a more convincing reading. For a second edition of the book, it might be too little on this small subject. Nevertheless, she can revise her digital edition professionally and release it again. The possible profit is great; she does not yet know what new insights actually emerge.

**How does Git help?** Anna compares the previous and revised file and documents the changes. She can mark important intermediate states with Git tags: One day is a name for a certain stored version, such as "seminar-2026" or "edition-1.0" . Thus Anna finds the version of the same time, while she is already working on it. An alternative interpretation can first try it separately and take over after testing.

**What is there to consider?** A typo correction is something else than a new edition decision. What has changed, why and who has contributed? The edition report must explain this. One day alone does not publish or archive anything and does not replace an understandable version specification or citation rule. Tags can be technically changed or deleted; published tags therefore treat Anna as fixed and assigns new names for revisions. Older quoted stands remain accessible or archived. Git does not update existing print copies or foreign downloads. In parallel book edition it should be clear which digital version corresponds to it.

**Action:** Set a simple version and citation rule. Mark important states with clearly named, briefly explained tags and transfer them explicitly to the hosting service; an ordinary push does not automatically transmit all tags. Set public tags only in the adjusted publication repository. Justify changes, get old release states and point out in the next release the differences to the book or the previous data version.

**Responsible:** Anna; if necessary technical counter-reading and publication/archive service

[Git: Mark booths with tags](https://git-scm.com/book/de/v2/Git-Grundlagen-Taggen)

## Teaching

ID: P01-C03

**Medium / medium**

Anna wants to show her students how an edition is created. A passage with two possible readings and an unfinished commentary would be closer to life than just the finished edition. The seminar can produce good queries and new observations. Without a specific date, this possibility is open at first.

**How does Git help?** Anna records the selected seminar version as her own named version. She can provide exactly this section for the group and later show how the comment has changed. Contributions from the course can be collected separately and checked before inclusion in the edition.

**What is there to consider?** Which passages are available in terms of technical and rights? Who may receive the excerpt? An internal teaching stand is not a public partial publication. Students need an understandable introduction and need to know how their suggestions are used and, if necessary, named. Commit numbers and times are not suitable performance measures.

**Action:** Preparing teaching, reading circuit and feedback channel; identifying quality status and taking over as well as recognising student contributions.

**Responsible:** Anna as teacher, student and if necessary teaching/infrastructure support

## Partial publication

ID: P01-C04

**Medium / medium**

One chapter is already well commented on, other parts still need months. Anna could already make the finished chapter usable. So those interested get a reliable section and can give their feedback. However, an announced approval does not mean that someone actually uses it.

**How does Git help?** A selected reviewed version is released. In a separate publication repository, Anna can only provide the released TEI files, metadata and documentation. Later additions are published as further comprehensible states; private work history does not have to come along.

**What is there to consider?** What really belongs to the released part? Does its index, image and comment references work without the rest? Are rights, terms of use and attribution clarified? Anna identifies missing parts and known limits. A data repo does not need a website yet, and a web offer does not replace the agreed archiving.

**Action:** Select a self-intelligible subset, check references and rights, attach README and version notice and document approval as well as archive transfer.

**Responsible:** Anna; if necessary expert review, metadata consulting and archive service

## Book publication

ID: P01-C08

**unclared / high**

Anna likes to imagine her edition as a book: a good sentence, careful review and a publishing house that reaches the right reader. A publishing request would be a real chance. However, she plans realistically with a TEI data publication and possibly a small website. A concrete publishing interest is not required in the model.

**How does Git help?** Anna can provide the publisher with a clearly defined verified version. Data and print edition can be derived from the same controlled source when an appropriate output path is set up. She can record the version for book edition and distinguish later digital revisions from it. Git does not communicate with the publisher and does not set up a book by herself.

**What is there to consider?** What services does the publisher take over, what costs and time arise for Anna? Can the TEI version, including commentaries, remain public and be revised later? Which rights should it grant, which has already been awarded or openly licensed? book typesetting, images and foreign contributions may have their own conditions. An effectively issued CC license can be taken back from users who comply with it: book and open data are not fundamentally incompatible. The concrete contract must fit with the already existing and planned publications.

**Action:** Clear early whether open data, minimal frontend and subsequent revisions are possible next to the book edition. Services, costs, rights, version assignment and correction with the publisher concretely agree; disclose existing licenses.

**Responsible:** Anna and interested publisher; expert advice on contract and rights issues

[Creative Commons: Choose Licenses](https://creativecommons.org/cc-license-your-work/) · [Creative Commons : Complementary Agreements] (https://creativecommons.org/faq/)

## Computer failure

ID: P01-R01

**Medium / high**

Anna's laptop doesn't start any more. This doesn't have to be the end of the edition work: what she regularly commits and has transmitted to the reliably operated Uni-GitLab is still there, including Git history. Last local changes and files that she didn't record in this backup path remain at risk.

**How does Git help?** Anna can create a new copy of the repos on a replacement computer and continue working on the last version transferred. Together with the externally operated repo, Git provides an effective way of backup for the captured files against computer loss. An additional independent copy improves backup.

**What is there to consider?** A commit only on the broken computer is not yet an external copy. Did Anna really push? How current is the version? Are pictures, notes, large external objects and required configurations also available? Anna also needs her new access options and the appropriate working environment. An existing copy should be practically tried out once.

**Action:** Regularly commit and push. Repo test in a fresh folder clone, check older stands as well as preview and document what is saved. Set a supplementary backup path for further files.

**Responsible:** Anna; the hosting service is responsible for its agreed operation, direct assistance only if necessary

## Repo access

ID: P01-R02

**unclared / high**

Anna's university connection ends while the edition is still growing. She wants to continue working and wonders if her previous repo access remains. An outgoing account is no reason to give up the data: The work inventory can come to another suitable place. What account rule applies is initially unexplained.

**How does Git help?** A complete local git copy contains the versioned files and their achievable history. Anna can transfer them to a new private repo and then regularly synchronize them again. For her small work path, a comprehensible guide, a new access and a test of the result are usually sufficient.

**What is there to consider?** Compare last booths before the end of access and record your own changes. Are all required industries, tags and external objects recorded? Issues, rights, automations and web publication are not automatically part of the Git files. The repo move also does not answer questions about oXygen license and consultation.

**Action:** Clear account rules in good time. After moving instructions, create a new destination, transfer data and history, test a fresh copy and document the new location.

**Responsible:** Anna on the basis of the instructions; competent authority clarifies the old access, technical assistance in special cases

## Advice

ID: P01-R03

**unclared / medium**

So far, Anna has been able to address advice at the university on a tricky XML question. After a job change, this contact may no longer be available. A small mistake can then cost disproportionately much edition time. Whether the consultation actually ends or remains another offer, she must clarify.

**How does Git help?** Versioned templates, schemas and understandable operating notes help Anna to find proven settings. It can show since which change a problem occurs, and prepare a small example for a query. A simple repo move remains possible with guidance even without direct advice.

**What is there to consider?** Git does not answer technical modelling questions and does not wait for a broken pipeline. Who can help with problems that Anna cannot solve alone? Can she start previewing and checking without the old server? Which recurring steps should be so well documented that she doesn't need anyone to do it?

**Action:** clarify consultation conditions, document important routines with examples and search for a realistic replacement contact for special cases. Keep the work path so easy that ongoing help is rarely necessary.

**Responsible:** Anna and previous or possible new counselling centre

## Tool change

ID: P01-R04

**unclared / medium**

Anna now likes to work in oXygen. Now it is unclear whether she may continue to use the campus permission after leaving. The familiar interface could fall away. Her TEI data will not become illegible, but changing tools and work routines needs attention.

**How does Git help?** TEI files, schema, templates and transformation rules can be further versioned. Anna can try another suitable XML tool on a copy and compare the results with the previous version. Git history is not bound to oXygen.

**What do you have to consider?** Clear license permission first instead of suspecting the absence. A replacement editor does not necessarily offer the same author view or help. Does input, validation and output still work? Proprietary settings may require customization. For the markdown path, this specific oXygen dependency is not required.

**Action:** Check permission; edit, validate and output a representative section in the alternative work path if required. Document differences and necessary steps in a short guide.

**Responsible:** Anna; License Management clarifies eligibility, point-by-point facility assistance if needed

## Confidence

ID: P01-R05

**Medium / high**

Anna and Mira write small XML comments while reading back: queries, half-finished thoughts and even a squeaky one. Before the release Anna deletes these notes. In the current file they are gone – in earlier Git stands they can still stand. An unchecked publication of the working repositorys could also publish the internal conversation.

**How does Git help?** The private working repository keeps changes for the collaboration. A separate publication repository can lead its own history of only verified approvals. Anna takes over cleaned files without the internal Git history; a mere clone or public work branch does not separate the history.

**What is there to consider?** Who can read the working data and old comments? Which metadata, file names or accompanying files are also internal? A private repo also requires a suitable reading circle. A new commit that deletes comments does not remove previous contents. Already distributed copies cannot be retrieved reliably. Scientific attribute should be retained when cleaning up.

**Action:** Delimit sensitive content before recording. Check files, metadata and achievable history for publication; take an adjusted export to the separate publication repository and check a fresh public copy.

**Responsible:** Anna and Mira for internal handling; Anna is responsible for the approval

[GitHub: Remove data from a repo story](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)

## Continuation

ID: P01-R06

**unclared / high**

Anna wants to finish the edition herself. Nevertheless, it is reassuring if after a long interruption someone could understand what already exists. A copy of the files is helpful, but her decisions, open questions and the way to output must also be understandable.

**How does Git help?** An available Repo-version with history keeps the stored work together. README, edition guidelines and a documented release status can be carried along. A named person can check, secure and edit the existing inventory if necessary.

**What is there to consider?** Who would actually be willing and entitled to assume responsibility? Is there a regulated access without passing on Anna's personal password? Are licenses, open tasks and required external files documented? Git does not explain any decisions taken in the mind or outside of the repos and does not determine succession.

**Action:** Arrange a consenting contact person or a carrier, clean accesses and create a small transfer package. Check with a test run whether another person can generate an output from it.

**Responsible:** Anna and expressly agreed representation or host institution

## Additional expenditure

ID: P01-R07

**Medium / medium**

Mira offers help, the students have ideas and after a partial release further hints come. Anna is pleased – and notes that she also has to provide answers, exams and integration. Support opens up possibilities, but initially also increases the need for coordination.

**How does Git help?** Small delimited suggestions, a comprehensible file comparison and collected queries facilitate the editing. Anna can examine and document proposals individually instead of laboriously collecting several commented files.

**What is there to consider?** A complicated Git procedure could also deter a helpful colleague. Is there enough mail or an commented section for this order? How much can be changed in parallel? Who answers questions, decides on contradictions and calls the contributors? Automatic tests do not replace the editorial review.

**Action:** Arrange a small order, a matching return channel and a realistic period of time. Do not trigger more contributions at the same time than Anna can understand.

**Responsible:** Anna and each participating participant

## Host Change

ID: P01-R08

**unclared / high**

So far, the preview runs comfortably on the Uni server. After a host change, the files are there, but the usual web output is not. Anna has to find out which processing was set up on the old service. Whether their output path depends on it is still unclear at the beginning.

**How does Git help?** Transformation rules, test scripts and a guide can be versioned together with the edition. If the output path is also locally executable, Anna can reuse it at the new location and compare results.

**What is there to consider?** Git does not transfer server accesses, secret settings or provided computing environments by itself. A service like GitHub Pages expects a static website; raw TEI files do not yet provide a ready-to-read view. Who maintains the template and which steps work without the previous host?

**Action:** Use a small example to test the local output path and note required tools. When changing, adjust host settings and web address separately; then check references and output.

**Responsible:** Anna using the operating instructions; installation and special cases with technical assistance

[GitHub Pages: static websites](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)

