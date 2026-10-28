# Git Manual of the Albrecht Edition

Fictional Albrecht project · independent sample document

**Version:** 1.1 · **Status:** Released project regulation · 21 October 2026

**Responsible:** Samir Demir · Scientific and Technical Editor

**approval:** Nora Seidel for the specialist editorials · Eva Brandt for the overall coordination

**Next exam:** 21 April 2027

This manual applies to all working groups of the Albrecht Edition. It describes the binding common practice and explicitly identifies recommendations. The currently valid version lies in the protected repository standards under governance/git-handbuch.md. New employees receive an introduction before the first productive commit.

## 0. Emergency aid: nothing hastily overwrite

H00 · Rule

In case of unclear version: Secure work, view git status and git diff and address the scientific-technical editors. Do not solve unclear conflicts by blindly taking over a page. If secrets or confidential information are accidentally introduced, immediately communicate IT and editorial staff – even if the current file has already been corrected.

No one rewrites shared or archived history on his own. The editorial team coordinates necessary interventions with IT and the competent authorities. Compressed access data are blocked; file deletion alone is not sufficient.

## 1. Validity and care

H01 · Rule

The working groups maintain texts in area repos. The common standard repo contains manuals, edition guidelines, schema/ODD, test rules, profile and transformation documentation. The central index is maintained in the register database. Its released snapshots are clearly linked to the text stands.

Samir supervises the manual together with a designated technical representation. Specialist editorials examine technical rules; Eva secures mandate and maintenance time. On April 21st and October 21st, the manual is reviewed, as well as after incidents as well as model and tool changes.

Proposals for modifications will receive a GOV-ticket with occasion, affected sections and scope. Technical and technical review are preceded by the approval. The released version will be tagged, explained in the team and announced in writing. Previous versions remain internally accessible. The manual does not extend any rights or analysis purposes of the employee agreement.

## Competence and attribution

H02 · Rule

Each assignment designates execution, scientific responsibility and editorial check. An assistant can implement a decision that Nora is responsible for; their technical work and Nora's scientific responsibility are documented separately. New readings or unclear assignments are decided professionally before they are accepted as reliable findings.

Personal Git identifiers such as alb-k7m42 remain stable and will not be remitted. Author and committer fields run these identifiers with a technical project address. The separate institutional identity register manages the assignment. Bots have their own identifiers. Scientific contributions and responsibility are identified in TEI metadata and contribution proofs. This information may allow conclusions; pseudonymous history is protected.

## 3. Equipment and accesses

H03 · Rule

Work repos are opened exclusively on institutionally managed, encrypted devices or in the remote working environment provided. This also applies to external contributors. Registration is made personal with multi-factor authentication; keys and tokens are not shared.

Private Git accounts, public forks, personal clouds and unregistered mirrors are excluded for internal inventory. IT runs the device and permission directory. Withdrawal of a server access does not delete local clones; their handling is part of the documented transfer.

Before access, the person in the participation and access directory is assigned to the appropriate task. Introduction, agreement, device sharing and permissions are confirmed. A technical Git training including the used oXygen-Git client belongs to this.

## 4. The Daily Way of Work

H04 · Rule

Check the correct workspace, branch and open file version before starting; retrieve the released version and synchronize it according to project procedures. Each task receives an ED, DATA or BUG ticket. Short branches of work are e.g. ed/ED-142 register subscription or fix/BUG-58 period.

Before the commit: Read Diff, validate affected TEI files, check file quantity and confidential content. A commit contains a related verifiable change. Text correction and global format conversion are separated. The commit message calls activity, object, concrete change and ticket, for example: reg(Letter-017): Correct recipient reference [ED-142].

A merge request bundles the target, ticket, technical justification, exams and open questions. main is protected. Changes in content require a second person who is responsible for technical matters; changes to the model, interface or test procedure additionally the technical editorial staff. Acquisition takes place with merge commit. Deviations require a documented approval; already shared contributions are not secretly rewritten.

## 5. TEI and oXygen

H05 · Rule

The editors distribute the shared oXygen project profile with assigned schema and documented program version. Author Mode is used for regular editing; text mode of the targeted XML control. After both, the diff is checked.

Existing characters, spacings, indentation and line endings are retained as long as the task does not require any change. Automatic complete formatting and hard automatic line breaks are disabled for edition files. Visual soft transition remains allowed. Profile changes are tested on representative files by opening, small modification, saving and diff.

An unintentionally reformatted file is not taken over at all. To secure the desired work first and to coordinate the restoration with the editors. Planned format migrations receive an isolated order. A green scheme test does not replace the control of the characters or the scientific examination.

## 6. Transitional rule: check again after reconciliation of registers

H06 · Rule

After re-importing from the comment interface, the modified comments are specifically checked for preserved strokes, protected spacing and date annotation. A period such as 1848–1849 must be maintained as a corresponding period of time. The automatically generated annotation layer for the index is checked before the ZX Q1.

The regression test includes range dash, protected distance, period marking and a factual comment correction without changing the time indication. It checks the entire back-and-back path. Nora confirms the professional expectation; Samir is responsible for the test.

Corrections go back to the relevant inventory. index snapshot, set, web finder and affected register issues are re-derived from the coordinated version and checked. Also a later purely factual correction goes through this control. Silent repairs exclusively in the flag are not completed correction.

H06 secures the time until technical acceptance of the revised comment tool. The tool change has its own order and regression test. After its probation, the need for additional control is re-evaluated and the manual adapted again.

## 7. Tests and editorial approval

H07 · Rule

Before each integration, XML well-formedness, project-specific schema, additional reference/consistency rules, Git ID check and security checks are performed. Formatting warnings are clarified. The examining person determines what has been professionally verified: source, identification, interpretation or side effects.

A technical test success does not give scientific or legal approval. Blocking protection tests are not routinely ignored. Necessary exceptions are documented on the basis of justification and responsible approval.

## 8. New tools and old data

H08 · Rule

New procedures are tested on a separate test stock. The order documents input, rule/program version, expected results, rights, data transmission, fault cases and return path. This also applies to OCR and LLM. Protected data do not go to external services without approval.

Editorially relevant proposals are examined professionally before taking over. In case of appropriate supervised procedures, control and withdrawal remain effective. For old data, it is recorded which collection with which standard version have been followed up and which exceptions have been examined professionally. New rules are not tacitly regarded as the yardstick of previous work.

## 9. Integration, publication and rights

H09 · Rule

The integration takes over audited data packets and an internal import manifest with source repo, source commit, index snapshot, check and permission note. Complete work stories remain in the protected origin repos. A data packet and a Git history are different transfer objects.

The publication environment generates its own public inventory with its own history from released sources. It does not take over internal commits. Nora is responsible for the scientific package release; the rights/publication office checks material rights and publishing conditions. Clara is included in the agreed production transfers.

Before publication, data, metadata, XML comments, images, generated files as well as all publicly accessible industries, tags, releases and artifacts are checked. An embargo triggers the object check. Only what meets the documented conditions is released. A file export alone is not a right check.

## Protection and preservation

H10 · Rule

IT secures central repos and required platform data daily; every week an institutionally separate backup is created. Monthly the recovery of a changing sample is logged, every year a complete tape setup. Database snapshots, additional binary files and necessary software components are included.

The volume manifest combines text, index, ZXq1, transformations, manual and profile versions as well as approvals. The scientific archive takes over citing publication packages and protected process packages separately. Process packages also contain required decision and process documentation; their accesses are regulated separately.

## 11. Incidents, departure and role change

H11 · Rule

Errors are reported with repo and stand identification, sensitive information in the confidential reporting channel. Notifications are first used to limit damage. Technical errors are rectified in a comprehensible manner; necessary security or data protection adjustments coordinate the competent body including controlled copies.

When leaving, tasks and open decisions are handed over, accesses blocked and local copies deleted or institutionally taken over according to IT instructions. Contributions remain visible in accordance with the agreed recognition rules. Data protection requests are examined separately; the departure does not automatically make the work history public or automatically pointless.

Local git stands and the .git directory remain protected against unauthorized access. Device loss, lost disks, accidental approvals or possibly copied data are reported immediately; a proven data flow is not awaited.

In case of role and institution changes, task, agreement and required access are re-examined prior to further work. Temporary exceptions for remaining accesses or copies need documented purpose, scope, protection, expiry date and approval of the overall coordination with the participation of the responsible bodies. IT documents the conversion and subsequent final control.

## 12. Recommendations and contact routes

H12 · Recommendation and Directory

Recommendation: often secure small understandable intermediates and avoid long unsynchronized work. Commit frequency is not a power measure. In case of uncertainty, include an expert early.

Git, profiles and handovers: scientific-technical editorial staff. Scientific decisions: responsible editorial board. Rights and publishing house: Legal/publication office. Security incidents: institutional IT service. Personal data and objections: data protection office and employee representation. The current contact list is protected in the project portal.

Binding attachments: Responsibilities matrix, Edition policy, ODD/schema, Verification rules, oXygen profile description, review template, rights directory, backup/archive profile and employee agreement. The released version of each installation is listed.

## Proof of change

- **1.0** First common working order: examination before handover, review, publication and security.
- **1.1** According to BUG-58: immediate return import control H06 released as transition rule; parallel tool revision and regression test commissioned. After acceptance of the tool, the rule is rechecked.
