# Software Qualification Test Requirements

## 문서 개요

이 일반 섹션은 테스트 요구사항 문서의 검증 범위를 설명합니다. 식별자로 시작하지 않으므로 색인 대상이 아닙니다.


## [SWQT_BLC_PEDAL_ON_001](@) 브레이크 페달 눌림 테스트

```yaml
Type: TestCase
Status: Draft
Verification: Test
```

- 테스트는 [stimulus_ignition_status](=)를 켜짐 상태로 설정하고 [observed_brake_pedal_status](=)를 눌림 상태로 설정했을 때 [observed_brake_lamp_request](=)가 활성화되는지 확인해야 합니다.

## [SWQT_BLC_PEDAL_OFF_001](@) 브레이크 페달 해제 테스트

```yaml
Type: TestCase
Status: Draft
Verification: Test
```

- 테스트는 [observed_brake_pedal_status](=)를 해제 상태로 설정했을 때 [observed_brake_lamp_request](=)가 비활성화되는지 확인해야 합니다.

## [SWQT_BLC_INPUT_DEBOUNCE_001](@) 브레이크 입력 디바운스 테스트

```yaml
Type: TestCase
Status: Draft
Verification: Test
```

- 테스트는 [stimulus_raw_brake_pedal_input](=)이 [debounce_time_ms](=)보다 짧게 변화할 때 [observed_brake_pedal_status](=)가 변경되지 않는지 확인해야 합니다.
- 테스트는 [stimulus_raw_brake_pedal_input](=)이 [debounce_time_ms](=) 이상 유지될 때 [observed_brake_pedal_status](=)가 변경되는지 확인해야 합니다.

## [SWQT_BLC_RESPONSE_TIME_001](@) 브레이크 램프 응답 시간 테스트

```yaml
Type: TestCase
Status: Draft
Verification: Test
```

- 테스트는 [stimulus_raw_brake_pedal_input](=)이 눌림 상태가 된 뒤 [measured_response_time_ms](=)가 100 ms 이하인지 확인해야 합니다.

## [SWQT_BLC_IGNITION_OFF_001](@) 점화 꺼짐 테스트

```yaml
Type: TestCase
Status: Draft
Verification: Test
```

- 테스트는 [stimulus_ignition_status](=)를 꺼짐 상태로 설정했을 때 [observed_brake_lamp_request](=)가 비활성화되는지 확인해야 합니다.

## [SWQT_BLC_INPUT_FAULT_001](@) 입력 고장 테스트

```yaml
Type: TestCase
Status: Draft
Verification: Test
```

- 테스트는 [stimulus_brake_pedal_fault_status](=)를 고장 상태로 설정했을 때 [observed_brake_lamp_request](=)와 [observed_brake_lamp_dtc_status](=)가 활성화되는지 확인해야 합니다.

## [SWQT_BLC_DIAGNOSTIC_RECOVERY_001](@) 진단 복구 테스트

```yaml
Type: TestCase
Status: Draft
Verification: Test
```

- 테스트는 [stimulus_brake_pedal_fault_status](=)를 정상 상태로 되돌렸을 때 [observed_brake_lamp_dtc_status](=)가 비활성화되는지 확인해야 합니다.

## [SWQT_BLC_STATUS_MESSAGE_001](@) 상태 메시지 테스트

```yaml
Type: TestCase
Status: Draft
Verification: Test
```

- 테스트는 [observed_vehicle_status_message](=)가 [observed_brake_pedal_status](=), [observed_brake_lamp_request](=), [observed_brake_lamp_dtc_status](=)를 포함하는지 확인해야 합니다.

## [SWQT_BLC_CYCLIC_EXECUTION_001](@) 주기 실행 테스트

```yaml
Type: TestCase
Status: Draft
Verification: Test
```

- 테스트는 [measured_task_period_ms](=)가 [control_task_period_ms](=)와 일치하는지 확인해야 합니다.

## [SWQT_BLC_SAFE_DEFAULT_001](@) 안전 기본값 테스트

```yaml
Type: TestCase
Status: Draft
Verification: Test
```

- 테스트는 입력 값이 유효하지 않을 때 [observed_brake_lamp_request](=)가 활성화되고 [observed_brake_lamp_dtc_status](=)가 활성화되는지 확인해야 합니다.

