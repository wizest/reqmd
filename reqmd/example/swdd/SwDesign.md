# Software Detailed Design

## 문서 개요

이 일반 섹션은 설계 문서의 구성 방식을 설명합니다. 식별자로 시작하지 않으므로 색인 대상이 아닙니다.


## [SWDD_BLC_INPUT_PROCESSING](@) 브레이크 입력 처리

```yaml
Type: Design
Status: Draft
Verification: Review
```

- 제어 주기가 도래할 때, 설계는 [=BrakePedalRaw](=)를 입력 드라이버에서 읽습니다.
- [=BrakePedalRaw](=)가 [debounce_time_ms](=) 이상 같은 상태인 경우, 설계는 [=BrakePedalDebounced](=)를 갱신합니다.

## [SWDD_BLC_OUTPUT_CONTROL](@) 브레이크 램프 출력 제어

```yaml
Type: Design
Status: Draft
Verification: Review
```

- [=IgnitionStatus](=)가 켜짐 상태이고 [=BrakePedalDebounced](=)가 눌림 상태인 경우, 설계는 [=BrakeLampReq](=)을 활성화합니다.
- [=IgnitionStatus](=)가 꺼짐 상태인 동안, 설계는 [=BrakeLampReq](=)을 비활성화합니다.
- [=BrakePedalFault](=)가 고장 상태인 경우, 설계는 [=BrakeLampReq](=)을 활성화합니다.

## [SWDD_BLC_DIAGNOSTIC_MANAGER](@) 진단 관리자

```yaml
Type: Design
Status: Draft
Verification: Review
```

- [=BrakePedalFault](=)가 고장 상태인 경우, 설계는 [=BLC_DTC_Status](=)를 활성화합니다.
- [=BrakePedalFault](=)가 정상 상태인 경우, 설계는 [=BLC_DTC_Status](=)를 비활성화합니다.

## [SWDD_BLC_STATUS_MESSAGE](@) 상태 메시지 구성

```yaml
Type: Design
Status: Draft
Verification: Review
```

- 상태 메시지를 구성할 때, 설계는 [=VehicleStatusMsg](=)에 [=BrakePedalDebounced](=), [=BrakeLampReq](=), [=BLC_DTC_Status](=)를 포함합니다.

## [SWDD_BLC_SCHEDULING](@) 주기 스케줄링

```yaml
Type: Design
Status: Draft
Verification: Review
```

- [control_task_period_ms](=) 주기가 도래할 때, 설계는 입력 처리, 출력 제어, 진단 관리자, 상태 메시지 구성을 순서대로 실행합니다.
- [=BrakeLampReq](=)를 갱신할 때, 설계는 [brake_lamp_response_time_ms](=) 조건을 만족하도록 같은 주기 안에서 갱신합니다.

## [SWDD_BLC_CALIBRATION](@) 보정값 관리

```yaml
Type: Design
Status: Draft
Verification: Review
```

- 보정값을 관리할 때, 설계는 [debounce_time_ms](=), [brake_lamp_response_time_ms](=), [control_task_period_ms](=)를 보정값 테이블에서 관리합니다.

## [SWDD_BLC_SAFE_DEFAULT](@) 안전 기본값

```yaml
Type: Design
Status: Draft
Verification: Review
```

- 입력 값이 유효하지 않은 경우, 설계는 [=BrakePedalFault](=)를 고장 상태로 설정하고 [=BrakeLampReq](=)을 활성화합니다.

