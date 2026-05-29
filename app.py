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

    str.image("https://mblogthumb-phinf.pstatic.net/MjAxOTAxMTBfMjI3/MDAxNTQ3MDgyMDU5NTMx.Vp-FwCyAhoC-JjJwrpEkO0-pOj-uZM3D8KqSwaqpQ20g.NEnY1ARZ3kc5smQVZZYY1hJ6xUKjr-2yU_Nm0tJYzNIg.JPEG.mombompt/ac81c6e64387b719b3a7818407ffab35.jpg?type=w800", caption="네발기기 흉추 로테이션 동작 가이드[출처: https://mblogthumb-phinf.pstatic.net/MjAxOTAxMTBfMjI3/MDAxNTQ3MDgyMDU5NTMx.Vp-FwCyAhoC-JjJwrpEkO0-pOj-uZM3D8KqSwaqpQ20g.NEnY1ARZ3kc5smQVZZYY1hJ6xUKjr-2yU_Nm0tJYzNIg.JPEG.mombompt/ac81c6e64387b719b3a7818407ffab35.jpg?type=w800]")
    
    str.success("**🏃 수행 방법**\n\n네발기기 자세에서 배꼽을 당겨 요추를 고정한 채, 한 손을 머리 뒤에 대고 상체만 하늘을 향해 회전합니다.")
    str.error("**🔍 파트너 체크리스트**\n\n허리의 비틀림이 없는지, 골반의 좌우 흔들림이 없는지 옆에서 밀착 모니터링하세요.")
   

# ③ 본운동 1 섹션
if exercise_menu == "전체 보기 / 개요" or exercise_menu == "③ 본운동 1️⃣":
    str.write("---")
    str.subheader("③ 본운동 1️⃣: Hook lying + 필라테스 링 드로우-인")
    str.caption("💪 도구: 필라테스 링 | ⏱️ 제한시간: 총 2분 (인당 60초) | 🔄 횟수: 4회 / 1세트")
    
    str.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQBnFe0M5_wS1ZawgpO_WIp9sNH0KEh59PSQ&s", caption="Hook lying 드로우-인 동작 가이드[출처: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQBnFe0M5_wS1ZawgpO_WIp9sNH0KEh59PSQ&s]")
    
    str.success("**🏃 수행 방법**\n\n갈고리 누운 자세에서 무릎 사이에 필라테스 링을 위치시키고, 숨을 내쉬며 링을 조임 cow 동시에 배꼽을 척추 쪽으로 당깁니다.")
    str.error("**🔍 파트너 체크리스트**\n\n허리가 과도하게 바닥을 누르거나 꺾이지 않는지, 엉덩이 근육이 과개입하지 않는지 확인하세요.")
    
# ③ 본운동 2 섹션
if exercise_menu == "전체 보기 / 개요" or exercise_menu == "③ 본운동 2️⃣":
    str.write("---")
    str.subheader("③ 본운동 2️⃣: 런지 + 세라밴드 PNF 패턴")
    str.caption("💪 도구: 세라밴드 | ⏱️ 제한시간: 총 3분 (인당 90초) | 🔄 횟수: 좌우 각 4회 / 1세트")
    
    str.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_yoHwwy8Uc2d4LzhWXHldtNyhwSkLgNPFfw&s", caption="미니 런지 + 세라밴드 PNF 동작 가이드[출처: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_yoHwwy8Uc2d4LzhWXHldtNyhwSkLgNPFfw&s]")
    
    str.success("**🏃 수행 방법**\n\n무릎 각도를 45°~60°(미니 런지)로 설정하여 골반 중립을 유지합니다. 복부 브레이싱을 잡은 채 세라밴드를 대각선 상방 패턴으로 당깁니다.")
    str.error("**🔍 파트너 체크리스트**\n\n대각선 저항을 주는 동안 환자의 요추가 과전만되거나 무릎 정렬이 깨지지 않는지 확인하세요.")
    
# ③ 본운동 3 섹션
if exercise_menu == "전체 보기 / 개요" or exercise_menu == "③ 본운동 3️⃣":
    str.write("---")
    str.subheader("③ 본운동 3️⃣: 시각 반응형 이중과제 교란 훈련")
    str.caption("💪 도구: 필라테스 링 | ⏱️ 제한시간: 총 3분 (인당 90초) | 🔄 횟수: 무작위 총 6회 / 1세트")

    str.image("blob:https://gemini.google.com/790820c4-a36b-4305-ad18-2c7b02a9d53c", caption="이중과제 동작 가이드[출처: 자체 제작 AI 시각자료]")
    
    str.success("**🏃 수행 방법**\n\n와이드 스쿼트 자세로 하체를 단단히 고정하고 링을 가슴 앞에 쥡니다. 파트너가 전방에서 무작위로 손을 뻗으면 흉추를 회전해 링 안으로 조준합니다.")
    str.error("**🔍 파트너 체크리스트**\n\n손을 뻗는 순간 요추에서 회전이나 미끄러지는 전단력이 발생하지 않는지 모니터링합니다.")

# ④ 마무리운동 섹션
if exercise_menu == "전체 보기 / 개요" or exercise_menu == "④ 마무리운동":
    str.write("---")
    str.subheader("④ 마무리운동: Standing Roll Down & Up with Ring")
    str.caption("💪 도구: 필라테스 링 | ⏱️ 제한시간: 총 2분 (인당 60초) | 🔄 횟수: 1회")

    str.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSF57QUYX1LtsaLGyZ6lPilQbF7GWsCFa5ZAw&s", caption="마무리 롤 업 앤 다운 덩작 가이드[출처: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSF57QUYX1LtsaLGyZ6lPilQbF7GWsCFa5ZAw&s]")
    
    str.success("**🏃 수행 방법**\n\n선 자세에서 숨을 내쉬며 머리→등→허리 순으로 말아 내려갑니다. 올라올 때는 링을 조이는 힘을 주며 아랫배를 당겨 척추를 하나씩 쌓아 올립니다.")
    str.error("**🔍 파트너 체크리스트**\n\n옆에서 관찰하며 환자가 올라올 때 링을 조이는 힘 덕분에 요추 불안정성 분절이 흔들리지 않는지 확인합니다.")
    
