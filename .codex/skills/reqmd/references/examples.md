# ReqMd Examples

Use these as compact before/after patterns.

## Add Software Requirement

User request: "Add a software requirement for brake lamp activation when the pedal is pressed."

Requirement body:

````markdown
## [SW_BLC_PEDAL_ON](@) Brake pedal pressed handling

```yaml
Type: Functional
Status: Draft
Priority: Must
Verification: Test
```

- The software shall activate [brake_lamp_request](=) when [ignition_status](=) is on and [brake_pedal_status](=) is pressed.
````

Identifier index:

```markdown
## [SW_BLC_PEDAL_ON](@#SW_BLC_PEDAL_ON)

- [SW_BLC_PEDAL_ON](SwReq.md#SW_BLC_PEDAL_ON)
- [SYS_BLC_PEDAL_ON](../sys/@#SYS_BLC_PEDAL_ON)
```

Helper index:

```markdown
## [brake_lamp_request](=#brake_lamp_request)

- [brake_lamp_request](SwReq.md#SW_BLC_PEDAL_ON)
- [=BrakeLampReq](../swdd/=#=BrakeLampReq)
```

## Repair Missing Fragment

Before:

```markdown
- [SYS_BLC_PEDAL_ON](../sys/@)
- [observed_brake_lamp_request](../swqt/=)
```

After:

```markdown
- [SYS_BLC_PEDAL_ON](../sys/@#SYS_BLC_PEDAL_ON)
- [observed_brake_lamp_request](../swqt/=#observed_brake_lamp_request)
```

## Remove Index YAML

Before:

````markdown
## [SW_BLC_PEDAL_ON](@#SW_BLC_PEDAL_ON)

- [SW_BLC_PEDAL_ON](SwReq.md#SW_BLC_PEDAL_ON)

```yaml
Status: Draft
```
````

After:

```markdown
## [SW_BLC_PEDAL_ON](@#SW_BLC_PEDAL_ON)

- [SW_BLC_PEDAL_ON](SwReq.md#SW_BLC_PEDAL_ON)
```
