import streamlit as str
import time

str.set_page_config(page_title="요추 불안정성 재활 가이드", page_icon="🎯", layout="centered")

# 🚨 사이드바 메뉴 구성 (타이머 + 운동 선택)
str.sidebar.header("📋 메뉴 컨트롤러")

# 1. 운동 섹션 선택 기능 추가
exercise_menu = str.sidebar.radio(
    "🏋️ 실습 운동 선택",
    [
        "전체 보기 / 개요",
        "② 준비운동",
        "③ 본운동 1️⃣",
        "③ 본운동 2️⃣",
        "③ 본운동 3️⃣",
        "④ 마무리운동"
    ]
)

str.sidebar.write("---")
str.sidebar.header("⏱️ 훈련 및 파트너 교대 타이머")
duration_preset = str.sidebar.selectbox("운동 시간 선택", ["2분 (준비/본운동1/마무리)", "3분 (본운동2/본운동3)", "직접 설정"])

if duration_preset == "2분 (준비/본운동1/마무리)":
    target_seconds = 60
elif duration_preset == "3분 (본운동2/본운동3)":
    target_seconds = 90
else:
    target_seconds = str.sidebar.number_input("시간 설정 (초)", min_value=10, max_value=600, value=60, step=10)

# 세션 상태 변수 초기화
if "timer_running" not in str.session_state:
    str.session_state.timer_running = False

# 타이머 제어 버튼 배치
col1, col2, col3 = str.sidebar.columns(3)

with col1:
    if str.button("⏱️ 시작"):
        str.session_state.timer_running = True

with col2:
    if str.button("🔄 교대"):
        str.session_state.timer_running = True
        str.rerun()

with col3:
    if str.button("⏹️ 정지"):
        str.session_state.timer_running = False
        str.rerun()

# 타이머 작동 로직
if str.session_state.timer_running:
    timer_slot = str.sidebar.empty()
    for remaining in range(target_seconds, -1, -1):
        if not str.session_state.timer_running:
            break
        mins, secs = divmod(remaining, 60)
        timer_slot.metric(label="⏳ 남은 시간", value=f"{mins:02d}:{secs:02d}")
        time.sleep(1)
    
    if str.session_state.timer_running:
        str.sidebar.success("🎉 운동 종료! 다음 파트너는 '교대' 버튼을 눌러주세요.")
        str.sidebar.audio("https://actions.google.com/sounds/v1/alarms/digital_watch_alarm_long.ogg", format="audio/ogg", autoplay=True)
        str.session_state.timer_running = False
    else:
        timer_slot.empty()
        str.sidebar.warning("⏱️ 타이머가 정지 및 초기화되었습니다.")


# 💻 메인 화면 콘텐츠 영역 (선택한 메뉴에 따라 화면을 다르게 보여줌)

# [공통] 메인 타이틀 및 개요
str.title("🎯 요추 불안정성 선수 재활 프로토콜")

if exercise_menu == "전체 보기 / 개요":
    str.info("■ **대상 선수**: 골프·야구 등 반복 회전 종목 선수 중 요추 불안정성/만성 요통(LBP) 환자\n\n■ **주요 목적**: 요추 고정(Stiffness) + 흉추 회전 분리(Dissociation) → 앞먹임 기전 재설정")
    str.write("👈 실습을 시작하려면 왼쪽 사이드바에서 원하는 **운동 단계**를 선택하고 **타이머**를 작동시켜 주세요!")

# ② 준비운동 섹션
if exercise_menu == "전체 보기 / 개요" or exercise_menu == "② 준비운동":
    str.write("---")
    str.subheader("② 준비운동: 드로우-인 네발기기 + 흉추 로테이션")
    str.caption("💪 도구: 없음 | ⏱️ 제한시간: 총 2분 (인당 60초) | 🔄 횟수: 좌우 각 3회 / 1세트")

    str.image("https://mblogthumb-phinf.pstatic.net/MjAxOTAxMTBfMjI3/MDAxNTQ3MDgyMDU5NTMx.Vp-FwCyAhoC-JjJwrpEkO0-pOj-uZM3D8KqSwaqpQ20g.NEnY1ARZ3kc5smQVZZYY1hJ6xUKjr-2yU_Nm0tJYzNIg.JPEG.mombompt/ac81c6e64387b719b3a7818407ffab35.jpg?type=w800", caption="네발기기 흉추 로테이션 동작 가이드[출처: 네이버 블로그]")
    
    str.success("""🏃 수행 방법
    
1. 손목은 어깨 아래, 무릎은 골반 아래에 오도록 네발기기 자세를 잡고 코로 숨을 마시며 척추 중립을 만듭니다.
2. 오른손을 뒷통수에 얹고, 지탱하는 왼팔로 바닥을 밀어내며 버틉니다.
3. 입으로 길게 내쉬는 호흡(Exhale)에 갈비뼈를 코르셋처럼 조이며, 골반과 허리는 미동도 하지 않게 고정한 채 오른쪽 가슴과 팔꿈치를 천장을 향해 회전시킵니다.
4. 다시 마시는 호흡에 천천히 시작 자세로 돌아옵니다. (좌우 동일 진행)""")
    str.error("**🔍 파트너 체크리스트**\n\n허리의 비틀림이 없는지, 골반의 좌우 흔들림이 없는지 옆에서 밀착 모니터링하세요.")
   

# ③ 본운동 1 섹션
if exercise_menu == "전체 보기 / 개요" or exercise_menu == "③ 본운동 1️⃣":
    str.write("---")
    str.subheader("③ 본운동 1️⃣: Hook lying + 필라테스 링 드로우-인")
    str.caption("💪 도구: 필라테스 링 | ⏱️ 제한시간: 총 2분 (인당 60초) | 🔄 횟수: 4회 / 1세트")
    
    str.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQBnFe0M5_wS1ZawgpO_WIp9sNH0KEh59PSQ&s", caption="Hook lying 드로우-인 동작 가이드 [출처: 구글 이미지]")
    
    str.success("""**🏃 수행 방법**

1. 누운 자세에서 무릎 사이에 필라테스 링을 끼우고 코로 마시며 갈비뼈를 넓힙니다.
2. 입으로 하- 내쉬는 호흡과 함께 무릎으로 링을 지그시 조임과 동시에, 배꼽을 등 뒤 바닥으로 쏙 집어넣어 허리 뒤 공간을 바닥에 가볍게 밀착(임프린팅)시킵니다.
3. 내쉬는 호흡이 끝날 때까지 3초간 유지한 후, 마시는 호흡에 힘을 풀며 돌아옵니다.""")
    str.error("**🔍 파트너 체크리스트**\n\n허리가 과도하게 바닥을 누르거나 꺾이지 않는지, 엉덩이 근육이 과개입하지 않는지 확인하세요.")
    
# ③ 본운동 2 섹션
if exercise_menu == "전체 보기 / 개요" or exercise_menu == "③ 본운동 2️⃣":
    str.write("---")
    str.subheader("③ 본운동 2️⃣: 런지 + 세라밴드 PNF 패턴")
    str.caption("💪 도구: 세라밴드 | ⏱️ 제한시간: 총 3분 (인당 90초) | 🔄 횟수: 좌우 각 4회 / 1세트")
    
    str.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_yoHwwy8Uc2d4LzhWXHldtNyhwSkLgNPFfw&s", caption="미니 런지 + 세라밴드 PNF 동작 가이드 [출처: 구글 이미지]")
    
    str.success("""**🏃 수행 방법**

1. 미니 런지 자세(무릎 각도 45°~60°)를 잡고 양손으로 세라밴드 끝을 잡아 시작 위치를 앞쪽 다리의 바깥쪽 골반 옆에 둡니다.
2. 코로 숨을 마시며 복부에 힘을 꽉 주어 몸통을 고정(브레이싱)합니다.
3. 입으로 강하게 내쉬면서 밴드를 반대쪽 대각선 위(어깨 너머) 방향으로 빠르게 당깁니다. 이때 몸통과 골반이 외력에 밀려 회전하지 않도록 정면을 유지하며 버틉니다.
4. 돌아올 때는 밴드의 탄성에 딸려가지 않도록 복부 힘으로 속도를 제어하며 천천히 시작 위치로 돌아옵니다.""")
    str.error("**🔍 파트너 체크리스트**\n\n대각선 저항을 주는 동안 환자의 요추가 과전만되거나 무릎 정렬이 깨지지 않는지 확인하세요.")
    
# ③ 본운동 3 섹션
if exercise_menu == "전체 보기 / 개요" or exercise_menu == "③ 본운동 3️⃣":
    str.write("---")
    str.subheader("③ 본운동 3️⃣: 시각 반응형 이중과제 교란 훈련")
    str.caption("💪 도구: 필라테스 링 | ⏱️ 제한시간: 총 3분 (인당 90초) | 🔄 횟수: 무작위 총 6회 / 1세트")

    # 🚨 [오류 수정] 웹 브라우저 호환 이미지 파일 주소로 안전하게 교체했습니다!
    str.image("https://totalworkout.fitness/img/exercise/1280/frame/10550.3.webp", caption="이중과제 마주보기 동작 가이드 [출처: https://totalworkout.fitness/img/exercise/1280/frame/10550.3.webp]")
    
    str.success("""**🏃 수행 방법**

1. 하프 스쿼트 자세로 서서 양손으로 필라테스 링을 잡고 가슴 앞에 위치시킵니다. 숨은 참지 않고 정상 호흡을 유지합니다.
2. 치료사가 전방에서 무작위로 손을 뻗으면, 그 손을 타겟 삼아 필라테스 링을 가슴 앞으로 곧게 뻗어 링 중앙에 치료사의 손이 들어오도록 조준합니다.
3. 이때 상지와 흉추는 타겟을 향해 움직이지만, 배꼽 아래 하체와 허리(요추)는 절대 회전하거나 흔들리지 않도록 강하게 강직성을 유지합니다.""")
    str.error("**🔍 파트너 체크리스트**\n\n손을 뻗는 순간 요추에서 회전이나 미끄러지는 전단력이 발생하지 않는지 모니터링합니다.")

# ④ 마무리운동 섹션
if exercise_menu == "전체 보기 / 개요" or exercise_menu == "④ 마무리운동":
    str.write("---")
    str.subheader("④ 마무리운동: Standing Roll Down & Up")
    str.caption("💪 도구: 없음 | ⏱️ 제한시간: 총 2분 (인당 60초) | 🔄 횟수: 1회")

    str.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSF57QUYX1LtsaLGyZ6lPilQbF7GWsCFa5ZAw&s", caption="마무리 롤 업 앤 다운 동작 가이드 [출처: 구글 이미지]")
    
    str.success("""**🏃 수행 방법**

1. 바르게 선 자세만듭니다.
2. 양 무릎을 미세하게 굽힌 상태(Micro-flexion)를 유지하여 부하를 고관절로 분산시킵니다.
3. 코로 숨을 마시시고, 입으로 내쉬면서(Exhale) 머리 → 등 → 허리 순서로 마디마디 말아 내려가되, 허리에 통증이 없는 범위(흉추~요추 상부 수준)까지만 하강을 제한합니다.
4. 아래에서 숨을 마시고, 다시 내쉬는 호흡에 아랫배를 척추 쪽으로 강하게 끌어당겨 척추를 아래부터 하나씩 쌓아 올리며 일어납니다.""")
    str.error("**🔍 파트너 체크리스트**\n\n옆에서 관찰하며 환자가 올라올 때 요추 불안정성 분절이 흔들리지 않는지 확인합니다.")
