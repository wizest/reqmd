# Software Requirements

## 문서 개요

이 일반 섹션은 소프트웨어 요구사항 문서의 범위를 설명합니다. 식별자로 시작하지 않으므로 색인 생성, 색인 검증, 추적성 계산의 대상이 아닙니다.


## [SW_BLC_CONTROL](@) 브레이크 램프 제어 소프트웨어

```yaml
Type: Container
Status: Draft
Priority: Must
Verification: Test
```

- 제어 주기가 도래한 경우, 브레이크 램프 제어 소프트웨어는 [brake_pedal_status](=), [ignition_status](=), [brake_pedal_fault_status](=)를 사용하여 [brake_lamp_request](=), [brake_lamp_dtc_status](=), [vehicle_status_message](=)를 갱신해야 합니다.

### [SW_BLC_PEDAL_ON](@) 브레이크 페달 눌림 처리

```yaml
Type: Functional
Status: Draft
Priority: Must
Verification: Test
```

- [ignition_status](=)가 켜짐 상태이고 [brake_pedal_status](=)가 눌림 상태인 경우, 소프트웨어는 [brake_lamp_request](=)를 활성화해야 합니다.

### [SW_BLC_PEDAL_OFF](@) 브레이크 페달 해제 처리

```yaml
Type: Functional
Status: Draft
Priority: Must
Verification: Test
```

- [brake_pedal_status](=)가 해제 상태이고 [brake_pedal_fault_status](=)가 정상 상태인 경우, 소프트웨어는 [brake_lamp_request](=)를 비활성화해야 합니다.

### [SW_BLC_INPUT_DEBOUNCE](@) 브레이크 입력 디바운스

```yaml
Type: Functional
Status: Draft
Priority: Must
Verification: Test
```

- [raw_brake_pedal_input](=)이 [debounce_time_ms](=) 이상 같은 상태로 유지된 경우, 소프트웨어는 [brake_pedal_status](=)를 갱신해야 합니다.

### [SW_BLC_RESPONSE_TIME](@) 브레이크 램프 요청 응답 시간

```yaml
Type: Performance
Status: Draft
Priority: Must
Verification: Test
```

- [raw_brake_pedal_input](=)이 눌림 상태가 된 경우, 소프트웨어는 [brake_lamp_response_time_ms](=) 이내에 [brake_lamp_request](=)를 활성화해야 합니다.

### [SW_BLC_IGNITION_OFF](@) 점화 꺼짐 처리

```yaml
Type: Functional
Status: Draft
Priority: Should
Verification: Test
```

- [ignition_status](=)가 꺼짐 상태인 동안, 소프트웨어는 [brake_lamp_request](=)를 비활성화해야 합니다.

### [SW_BLC_INPUT_FAULT](@) 브레이크 입력 고장 처리

```yaml
Type: Safety
Status: Draft
Priority: Must
Verification: Test
```

- [brake_pedal_fault_status](=)가 고장 상태인 경우, 소프트웨어는 [brake_lamp_request](=)를 활성화하고 [brake_lamp_dtc_status](=)를 활성화해야 합니다.

### [SW_BLC_DIAGNOSTIC_RECOVERY](@) 브레이크 입력 고장 복구

```yaml
Type: Safety
Status: Draft
Priority: Should
Verification: Test
```

- [brake_pedal_fault_status](=)가 정상 상태로 돌아온 경우, 소프트웨어는 [brake_lamp_dtc_status](=)를 비활성화해야 합니다.

### [SW_BLC_STATUS_COMMUNICATION](@) 상태 메시지 송신

```yaml
Type: Functional
Status: Draft
Priority: Should
Verification: Test
```

- 상태 메시지를 구성할 때, 소프트웨어는 [brake_lamp_request](=), [brake_pedal_status](=), [brake_lamp_dtc_status](=)를 [vehicle_status_message](=)에 포함해야 합니다.

### [SW_BLC_CYCLIC_EXECUTION](@) 주기 실행

```yaml
Type: Timing
Status: Draft
Priority: Must
Verification: Test
```

- [control_task_period_ms](=) 주기가 도래할 때, 소프트웨어는 입력을 읽고 출력을 갱신해야 합니다.

