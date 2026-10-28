# Recommendations at a glance
### How we would begin
We organise TEI files, the model, queries, transformations and documentation as a traceable collection in Git. XML tools provide query capabilities. We add a database service when it brings a concrete benefit. An existing, supported institutional service can make sense even for a small project.
## Git and XML tools
Git holds the authoritative collection. Editors compare and check changes, record them as commits and transfer them to the shared repository. XML tools read the files. Publication can be generated statically; a running application is also possible.
## Git leads; the database provides access
Git holds the authoritative edition data. A checked import builds the database collection. The database serves queries and the interface. Editorial corrections return to Git through the agreed review process; the database is then updated. There is no uncontrolled second place for edits.
## Edit in a database and connect it to Git
An existing database interface remains the authoritative editing environment. A defined export passes checked changes to Git, which versions the exported data and associated programs. Editing exported files and the database simultaneously requires an agreed reconciliation process.
A database solution can also be configured with versioning. This does not automatically create a connected history of changes to texts, schemas and programs. We recommend preserving that history with Git and using a database for its concrete benefits.
## What remains after the project?
-
Edition data
: TEI, metadata, links, model, documentation and rights.
-
Publication output
: The actual web edition, indexes, search index and any print/PDF output. Identify indispensable external services.
-
Production and process history
: Relevant Git history, queries, transformations, tests, configurations, dependencies and decision notes.
Static or dynamic is a separate decision. Git can supply a running application; a database can generate static outputs. A Git repository replaces neither an archive service nor funding for a running system.
Editorial basis: the two supplied working documents on Git and XML databases. Text, translation, schematic diagrams and implementation were created with AI assistance. Version 1.0 · 28 October 2026. Diagrams show workflow models, not an actual installation.
