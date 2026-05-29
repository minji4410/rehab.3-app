import streamlit as str
import time

str.set_page_config(page_title="요추 불안정성 재활 가이드", page_icon="🎯", layout="centered")

str.title("🎯 요추 불안정성 선수 재활 프로토콜")

str.info("■ **대상 선수**: 골프·야구 등 반복 회전 종목 선수 중 요추 불안정성/만성 요통(LBP) 환자\n\n■ **주요 목적**: 요추 고정(Stiffness) + 흉추 회전 분리(Dissociation) → 앞먹임 기전 재설정")

str.write("---")

# 🚨 사이드바 타이머 영역
str.sidebar.header("⏱️ 훈련 및 파트너 교대 타이머")
duration_preset = str.sidebar.selectbox("운동 시간 선택", ["2분 (준비/본운동1/마무리)", "3분 (본운동2/본운동3)", "직접 설정"])

# 한 명당 수행할 시간 세팅 (2분 선택 시 인당 60초, 3분 선택 시 인당 90초)
if duration_preset == "2분 (준비/본운동1/마무리)":
    target_seconds = 60
elif duration_preset == "3분 (본운동2/본운동3)":
    target_seconds = 90
else:
    target_seconds = str.sidebar.number_input("시간 설정 (초)", min_value=10, max_value=600, value=60, step=10)

# 세션 상태 변수 초기화 (중간에 리셋하고 다시 시작할 수 있도록)
if "timer_running" not in str.session_state:
    str.session_state.timer_running = False

col1, col2 = str.sidebar.columns(2)

with col1:
    if str.button("⏱️ 타이머 시작"):
        str.session_state.timer_running = True

with col2:
    # 이 버튼을 누르면 현재 가던 타이머를 무시하고, 설정된 시간(60초/90초)으로 싹 리셋해서 처음부터 다시 돌려줌!
    if str.button("🔄 다음 파트너 시작"):
        str.session_state.timer_running = True
        str.rerun()

# 타이머 작동 로직
if str.session_state.timer_running:
    timer_slot = str.sidebar.empty()
    for remaining in range(target_seconds, -1, -1):
        mins, secs = divmod(remaining, 60)
        timer_slot.metric(label="⏳ 남은 시간", value=f"{mins:02d}:{secs:02d}")
        time.sleep(1)
    
    str.sidebar.success("🎉 운동 종료! 다음 파트너는 '다음 파트너 시작' 버튼을 눌러주세요.")
    str.session_state.timer_running = False

# ② 준비운동 섹션
str.subheader("② 준비운동: 드로우-인 네발기기 + 흉추 로테이션")
str.caption("💪 도구: 없음 | ⏱️ 제한시간: 총 2분 (인당 60초) | 🔄 횟수: 좌우 각 3회 / 1세트")
str.success("**🏃 수행 방법**\n\n네발기기 자세에서 배꼽을 당겨 요추를 고정한 채, 한 손을 머리 뒤에 대고 상체만 하늘을 향해 회전합니다.")
str.error("**🔍 파트너 체크리스트**\n\n허리의 비틀림이 없는지, 골반의 좌우 흔들림이 없는지 옆에서 밀착 모니터링하세요.")
str.warning("**🗣️ 치료사 큐잉**\n\n“허리 위 막대기가 굴러떨어지지 않게 고정하세요.”, “골반은 수평을 유지하고 가슴만 천장을 향해 돌립니다.”")

str.write("---")

# ③ 본운동 1 섹션
str.subheader("③ 본운동 1️⃣: Hook lying + 필라테스 링 드로우-인")
str.caption("💪 도구: 필라테스 링 | ⏱️ 제한시간: 총 2분 (인당 60초) | 🔄 횟수: 4회 / 1세트")
str.success("**🏃 수행 방법**\n\n갈고리 누운 자세에서 무릎 사이에 필라테스 링을 위치시키고, 숨을 내쉬며 링을 조임과 동시에 배꼽을 척추 쪽으로 당깁니다.")
str.error("**🔍 파트너 체크리스트**\n\n허리가 과도하게 바닥을 누르거나 꺾이지 않는지, 엉덩이 근육이 과개입하지 않는지 확인하세요.")
str.warning("**🗣️ 치료사 큐잉**\n\n“허리 바닥에 가볍게 밀착되는 임프린팅 유지! 지퍼 채우듯 아랫배와 허벅지 안쪽 동시에 조이세요.”")

str.write("---")

# ③ 본운동 2 섹션
str.subheader("③ 본운동 2️⃣: 런지 + 세라밴드 PNF 패턴")
str.caption("💪 도구: 세라밴드 | ⏱️ 제한시간: 총 3분 (인당 90초) | 🔄 횟수: 좌우 각 4회 / 1세트")
str.success("**🏃 수행 방법**\n\n무릎 각도를 45°~60°(미니 런지)로 설정하여 골반 중립을 유지합니다. 복부 브레이싱을 잡은 채 세라밴드를 대각선 상방 패턴으로 당깁니다.")
str.error("**🔍 파트너 체크리스트**\n\n대각선 저항을 주는 동안 환자의 요추가 과전만되거나 무릎 정렬이 깨지지 않는지 확인하세요.")
str.warning("**🗣️ 치료사 큐잉**\n\n“외력이 몸을 흔들어도 체간의 강직성을 유지해 버티세요.”, “앞쪽 무릎과 발가락이 일직선 정렬에서 무너지지 않게 하세요.”")

str.write("---")

# ③ 본운동 3 섹션
str.subheader("③ 본운동 3️⃣: 시각 반응형 이중과제 교란 훈련")
str.caption("💪 도구: 필라테스 링 | ⏱️ 제한시간: 총 3분 (인당 90초) | 🔄 횟수: 무작위 총 6회 / 1세트")
str.success("**🏃 수행 방법**\n\n와이드 스쿼트 자세로 하체를 단단히 고정하고 링을 가슴 앞에 쥡니다. 파트너가 전방에서 무작위로 손을 뻗으면 흉추를 회전해 링 안으로 조준합니다.")
str.error("**🔍 파트너 체크리스트**\n\n손을 뻗는 순간 요추에서 회전이나 미끄러지는 전단력이 발생하지 않는지 모니터링합니다.")
str.warning("**🗣️ 치료사 큐잉**\n\n“치료사의 손 움직임을 끝까지 보세요.”, “손이 나오는 순간 배에 힘을 주어 몸통은 미동도 없이 타겟을 조준하세요.”")

str.write("---")

# ④ 마무리운동 섹션
str.subheader("④ 마무리운동: Standing Roll Down & Up with Ring")
str.caption("💪 도구: 필라테스 링 | ⏱️ 제한시간: 총 2분 (인당 60초) | 🔄 횟수: 1회")
str.success("**🏃 수행 방법**\n\n선 자세에서 숨을 내쉬며 머리→등→허리 순으로 말아 내려갑니다. 올라올 때는 링을 조이는 힘을 주며 아랫배를 당겨 척추를 하나씩 쌓아 올립니다.")
str.error("**🔍 파트너 체크리스트**\n\n옆에서 관찰하며 환자가 올라올 때 링을 조이는 힘 덕분에 요추 불안정성 분절이 흔들리지 않는지 확인합니다.")
str.warning("**🗣️ 치료사 큐잉**\n\n“내려갈 때는 자전거 체인처럼 마디마디 내려가세요.”, “올라올 때는 링을 가볍게 조이면서 아랫배를 쏙 집어넣는 힘으로 올라옵니다.”")
