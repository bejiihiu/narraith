# Security policy

## What is in scope

Narraith is a set of instructions and reference documents. It does not execute user input, make network
requests, or store data. The realistic security concerns are:

- **Prompt injection through cited material.** The skill tells a model to read files in this repository.
  A contributed file that contains instructions aimed at the model — rather than craft content — is a
  supply-chain problem for every user.
- **Unsafe examples.** Prose examples that normalise violence, targeted harassment, or instructions for
  harm.
- **Leaked data.** A contribution that includes a real person's private information, a credential, or
  unpublished third-party text.

## Reporting

Open a private security advisory on the repository, or email the maintainer listed in `CITATION.cff`.
Do not open a public issue for a prompt-injection payload or a leaked secret.

Include: the file, the quoted fragment, what it would cause a model to do, and how you found it.

## Response

We aim to acknowledge within a week, remove or patch the content, and credit the reporter unless they
ask otherwise. Because the skill is loaded by other people's models, a confirmed injection is treated as
a release-blocking defect, not a documentation nit.
