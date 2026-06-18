# ReqMd Syntax

ReqMd is plain Markdown with project conventions. Do not invent non-Markdown syntax.

## Document Sections

Requirement documents may contain two section kinds:

- RequirementSection: starts with an identifier link such as `## [SW_BLC_PEDAL_ON](@)`.
- GeneralSection: does not start with an identifier and is not used for index generation, index validation, or traceability calculation.

Requirement attributes are YAML blocks inside RequirementSection content. Do not add YAML attributes to `@.md` or `=.md`.

RequirementBody content is written with EARS (Easy Approach to Requirements Syntax) style requirement statements. Use a clear subject and response, and put triggers, states, options, or exception conditions at the front of the sentence when they apply.

````markdown
## [SW_BLC_PEDAL_ON](@) Brake pedal pressed handling

```yaml
Type: Functional
Status: Draft
```

- When [brake_pedal_status](=) is pressed, the controller shall set [brake_lamp_request](=) active.

## Notes

This GeneralSection is not indexed.
````

## Identifier

- Syntax: `[IDENTIFIER](@)` or `[IDENTIFIER](path/@)`.
- Use `SCREAMING_SNAKE_CASE`.
- Regex: `[A-Z][A-Z0-9_]*`.
- Use stable names; do not rename just because a title changes.
- In index files, always include a fragment.
- Index heading links point to source document sections.
- Index body links point to other index sections, for example `@#sw_blc_pedal_on` or `path/@#sys_blc_pedal_on`.

## Helper

- Syntax: `[helper](=)` or `[helper](path/=)`.
- General helpers use `snake_case`.
- Regex: `[a-z][a-z0-9_]*`.
- Implementation helpers start with `=`, for example `[=BrakeLampReq](=)`.
- Do not force implementation helpers into `snake_case`; preserve actual code/model names.
- In index files, always include a fragment.
- Helper index headings are plain helper names without links.
- Index body links point to other index sections, for example `=#brake_lamp_request` or `path/=#brakelampreq`.

## Attribute

- Attributes are YAML code blocks in RequirementSection content.
- Never add YAML blocks to `@.md` or `=.md`.
- Prefer stable field names such as `Type`, `Status`, `Priority`, `Source`, `Verification`, `Variant`, and `Owner`.

## Identifier Index

File name: `@.md`.

```markdown
## [SW_BLC_PEDAL_ON](SwReq.md#sw_blc_pedal_on-brake-pedal-pressed-handling)

- [SYS_BLC_PEDAL_ON](../sys/@#sys_blc_pedal_on)
- [SWQT_BLC_PEDAL_ON_001](../swqt/@#swqt_blc_pedal_on_001)
- [brake_pedal_status](=#brake_pedal_status)
- [brake_lamp_request](=#brake_lamp_request)
```

## Helper Index

File name: `=.md`.

```markdown
## brake_lamp_request

- [=BrakeLampReq](../swdd/=#brakelampreq)
- [observed_brake_lamp_request](../swqt/=#observed_brake_lamp_request)
- [SW_BLC_PEDAL_ON](@#sw_blc_pedal_on)
```
