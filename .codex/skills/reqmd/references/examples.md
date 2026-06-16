# ReqMd Examples

Use these as compact before/after patterns.

## Add Software Requirement

User request: "Add a software requirement for brake lamp activation when the pedal is pressed."

Requirement document:

````markdown
## [SW_BLC_PEDAL_ON](@) Brake pedal pressed handling

```yaml
Type: Functional
Status: Draft
Priority: Must
Verification: Test
```

- When [ignition_status](=) is on and [brake_pedal_status](=) is pressed, the software shall activate [brake_lamp_request](=).

## Notes

This GeneralSection is not indexed.
````

Identifier index:

```markdown
## [SW_BLC_PEDAL_ON](SwReq.md#sw_blc_pedal_on-brake-pedal-pressed-handling)

- [SYS_BLC_PEDAL_ON](../sys/@#sys_blc_pedal_on)
```

Helper index:

```markdown
## [brake_lamp_request](SwReq.md#sw_blc_pedal_on-brake-pedal-pressed-handling)

- [=BrakeLampReq](../swdd/=#brakelampreq)
```

## Repair Missing Fragment

Before:

```markdown
- [SYS_BLC_PEDAL_ON](../sys/@)
- [observed_brake_lamp_request](../swqt/=)
```

After:

```markdown
- [SYS_BLC_PEDAL_ON](../sys/@#sys_blc_pedal_on)
- [observed_brake_lamp_request](../swqt/=#observed_brake_lamp_request)
```

## Ignore GeneralSection Helpers

Before:

````markdown
## [SW_BLC_PEDAL_ON](@) Brake pedal pressed handling

- When [brake_pedal_status](=) is pressed, the software shall set [brake_lamp_request](=) active.

## Notes

- [draft_signal_name](=) is only a note and is not indexed.
````

After:

```markdown
## [brake_lamp_request](SwReq.md#sw_blc_pedal_on-brake-pedal-pressed-handling)

```

Do not create a `=.md` section for `draft_signal_name` unless it appears in a RequirementSection or the user explicitly promotes it to a requirement/design/test helper.

## Remove Index YAML

Before:

````markdown
## [SW_BLC_PEDAL_ON](SwReq.md#sw_blc_pedal_on-brake-pedal-pressed-handling)

```yaml
Status: Draft
```
````

After:

```markdown
## [SW_BLC_PEDAL_ON](SwReq.md#sw_blc_pedal_on-brake-pedal-pressed-handling)

```
