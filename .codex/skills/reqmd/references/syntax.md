# ReqMd Syntax

ReqMd is plain Markdown with project conventions. Do not invent non-Markdown syntax.

## Requirement Body

Requirement documents are normal `.md` files except `@.md` and `=.md`.

````markdown
## [SW_BLC_PEDAL_ON](@) Brake pedal pressed handling

```yaml
Type: Functional
Status: Draft
Priority: Must
Verification: Test
```

- The controller shall set [brake_lamp_request](=) active when [brake_pedal_status](=) is pressed.
````

## Identifier

- Syntax: `[IDENTIFIER](@)` or `[IDENTIFIER](path/@)`.
- Use `SCREAMING_SNAKE_CASE`.
- Regex: `[A-Z][A-Z0-9_]*`.
- Use stable names; do not rename just because a title changes.
- In index files, always include a fragment. Index heading links point to source document sections. Index body links point to other index sections, for example `@#sw_blc_pedal_on` or `path/@#sys_blc_pedal_on`.

## Helper

- Syntax: `[helper](=)` or `[helper](path/=)`.
- General helpers use `snake_case`.
- Regex: `[a-z][a-z0-9_]*`.
- Implementation helpers start with `=`, for example `[=BrakeLampReq](=)`.
- Do not force implementation helpers into `snake_case`; preserve actual code/model names.
- In index files, always include a fragment. Index heading links point to source document sections. Index body links point to other index sections, for example `=#brake_lamp_request` or `path/=#brakelampreq`.

## Attribute

- Attributes are YAML code blocks in requirement bodies only.
- Never add YAML blocks to `@.md` or `=.md`.
- Prefer stable field names such as `Type`, `Status`, `Priority`, `Source`, `Verification`, `Variant`, and `Owner`.

## Identifier Index

File name: `@.md`.

```markdown
## [SW_BLC_PEDAL_ON](SwReq.md#sw_blc_pedal_on-brake-pedal-pressed-handling)

- [SYS_BLC_PEDAL_ON](../sys/@#sys_blc_pedal_on)
- [SWQT_BLC_PEDAL_ON_001](../swqt/@#swqt_blc_pedal_on_001)
```

## Helper Index

File name: `=.md`.

```markdown
## [brake_lamp_request](SwReq.md#sw_blc_pedal_on-brake-pedal-pressed-handling)

- [=BrakeLampReq](../swdd/=#brakelampreq)
- [observed_brake_lamp_request](../swqt/=#observed_brake_lamp_request)
```
