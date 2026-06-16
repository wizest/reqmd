# System Requirements

## 문서 개요

이 일반 섹션은 시스템 요구사항 문서의 배경을 설명합니다. 식별자로 시작하지 않으므로 `@.md`, `=.md` 색인의 대상이 아닙니다.


## [SYS_BLC_CONTROL](@) 브레이크 램프 제어

```yaml
Type: Container
Status: Approved
Priority: Must
Verification: Test
```

- 차량은 운전자의 제동 의도를 감지하여 [brake_lamp_state](=)를 제어해야 합니다.

### [SYS_BLC_PEDAL_ON](@) 브레이크 페달 눌림 시 램프 점등

```yaml
Type: Functional
Status: Approved
Priority: Must
Verification: Test
```

- 차량은 [brake_pedal_status](=)가 눌림 상태이면 [brake_lamp_state](=)를 켜야 합니다.

### [SYS_BLC_PEDAL_OFF](@) 브레이크 페달 해제 시 램프 소등

```yaml
Type: Functional
Status: Approved
Priority: Must
Verification: Test
```

- 차량은 [brake_pedal_status](=)가 해제 상태이면 [brake_lamp_state](=)를 꺼야 합니다.

### [SYS_BLC_RESPONSE_TIME](@) 브레이크 램프 응답 시간

```yaml
Type: Performance
Status: Approved
Priority: Must
Verification: Test
```

- 차량은 [brake_pedal_status](=)가 눌림 상태가 된 뒤 [brake_lamp_response_time_ms](=) 이내에 [brake_lamp_state](=)를 켜야 합니다.

### [SYS_BLC_IGNITION_OFF](@) 점화 꺼짐 상태의 램프 요청

```yaml
Type: Functional
Status: Approved
Priority: Should
Verification: Test
```

- 차량은 [ignition_status](=)가 꺼짐 상태이면 [brake_lamp_state](=)를 꺼진 상태로 유지해야 합니다.

### [SYS_BLC_INPUT_FAULT](@) 브레이크 입력 고장 처리

```yaml
Type: Safety
Status: Approved
Priority: Must
Verification: Test
```

- 차량은 [brake_pedal_fault_status](=)가 고장 상태이면 [brake_lamp_state](=)를 켜고 [brake_lamp_dtc_status](=)를 활성화해야 합니다.

### [SYS_BLC_STATUS_COMMUNICATION](@) 브레이크 램프 상태 통신

```yaml
Type: Functional
Status: Approved
Priority: Should
Verification: Test
```

- 차량은 [brake_lamp_state](=)와 [brake_lamp_dtc_status](=)를 [vehicle_status_message](=)로 전송해야 합니다.

