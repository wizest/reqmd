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
- In index files, always include a fragment: `@#IDENTIFIER` or `path/@#IDENTIFIER`.

## Helper

- Syntax: `[helper](=)` or `[helper](path/=)`.
- General helpers use `snake_case`.
- Regex: `[a-z][a-z0-9_]*`.
- Implementation helpers start with `=`, for example `[=BrakeLampReq](=)`.
- Do not force implementation helpers into `snake_case`; preserve actual code/model names.
- In index files, always include a fragment: `=#helper` or `path/=#helper`.

## Attribute

- Attributes are YAML code blocks in requirement bodies only.
- Never add YAML blocks to `@.md` or `=.md`.
- Prefer stable field names such as `Type`, `Status`, `Priority`, `Source`, `Verification`, `Variant`, and `Owner`.

## Identifier Index

File name: `@.md`.

```markdown
## [SW_BLC_PEDAL_ON](@#SW_BLC_PEDAL_ON)

- [SW_BLC_PEDAL_ON](SwReq.md#SW_BLC_PEDAL_ON)
- [SYS_BLC_PEDAL_ON](../sys/@#SYS_BLC_PEDAL_ON)
- [SWQT_BLC_PEDAL_ON_001](../swqt/@#SWQT_BLC_PEDAL_ON_001)
```

## Helper Index

File name: `=.md`.

```markdown
## [brake_lamp_request](=#brake_lamp_request)

- [brake_lamp_request](SwReq.md#SW_BLC_PEDAL_ON)
- [=BrakeLampReq](../swdd/=#=BrakeLampReq)
- [observed_brake_lamp_request](../swqt/=#observed_brake_lamp_request)
```
