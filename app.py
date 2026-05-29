import streamlit as str
import time

# 페이지 설정
str.set_page_config(page_title="요추 불안정성 재활 가이드", page_icon="🎯", layout="centered")

# 세션 상태 변수 초기화 (여러 타이머가 서로 간섭하지 않도록 제어)
if "active_timer" not in str.session_state:
    str.session_state.active_timer = None
if "timer_remaining" not in str.session_state:
    str.session_state.timer_remaining = 0
if "timer_running" not in str.session_state:
    str.session_state.timer_running = False

# 공통 타이머 실행 함수
def run_timer(timer_id, seconds):
    str.session_state.active_timer = timer_id
    str.session_state.timer_remaining = seconds
    str.session_state.timer_running = True

# 타이머 정지 함수
def stop_timer():
    str.session_state.timer_running = False
    str.session_state.active_timer = None
    str.rerun()

# --- 🚨 상단 고정 실시간 카운트다운 알림창 ---
if str.session_state.timer_running and str.session_state.timer_remaining > 0:
    placeholder = str.empty()
    with placeholder.container():
        mins, secs = divmod(str.session_state.timer_remaining, 60)
        str.warning(f"⏱️ **현재 측정 중**: [{str.session_state.active_timer}] — ⏳ **남은 시간: {mins:02d}:{secs:02d}**")
        
        if str.button("⏹️ 타이머 정지 / 삭제", key="global_stop"):
            stop_timer()
            
    time.sleep(1)
    str.session_state.timer_remaining -= 1
    
    if str.session_state.timer_remaining < 0:
        str.session_state.timer_running = False
        str.success(f"🎉 [{str.session_state.active_timer}] 제한시간이 끝났습니다! 파트너와 교대하세요.")
        # 타이머 종료 음원 재생
        str.audio("https://actions.google.com/sounds/v1/alarms/digital_watch_alarm_long.ogg", format="audio/ogg", autoplay=True)
        str.session_state.active_timer = None
    str.rerun()


# 💻 메인 화면 콘텐츠 영역
str.title("🎯 요추 불안정성 선수 재활 프로토콜")
str.info("■ **대상 선수**: 골프·야구 등 반복 회전 종목 선수 중 요추 불안정성/만성 요통(LBP) 환자\n\n■ **주요 목적**: 요추 고정(Stiffness) + 흉추 회전 분리(Dissociation) → 앞먹임 기전 재설정")
str.write("💡 아래로 스크롤하며 순서대로 실습을 진행하세요. 파트너 체크리스트 밑에서 전용 타이머를 바로 작동할 수 있습니다.")


# ==========================================
# ② 준비운동 섹션
# ==========================================
str.write("---")
str.subheader("② 준비운동: 드로우-인 네발기기 + 흉추 로테이션")
str.caption("💪 도구: 없음 | 🔄 횟수: 좌우 각 3회 / 1세트")
str.image("https://mblogthumb-phinf.pstatic.net/MjAxOTAxMTBfMjI3/MDAxNTQ3MDgyMDU5NTMx.Vp-FwCyAhoC-JjJwrpEkO0-pOj-uZM3D8KqSwaqpQ20g.NEnY1ARZ3kc5smQVZZYY1hJ6xUKjr-2yU_Nm0tJYzNIg.JPEG.mombompt/ac81c6e64387b719b3a7818407ffab35.jpg?type=w800", caption="네발기기 흉추 로테이션 동작 가이드 [출처:자체 제작 AI 시각자료]")
str.success("**🏃 수행 방법**\n\n네발기기 자세에서 배꼽을 당겨 요추를 고정한 채, 한 손을 머리 뒤에 대고 상체만 하늘을 향해 회전합니다.")
str.error("**🔍 파트너 체크리스트**\n\n허리의 비틀림이 없는지, 골반의 좌우 흔들림이 없는지 옆에서 밀착 모니터링하세요.")

# ⏱️ 준비운동 전용 타이머 배치
if str.button("⏱️ 준비운동 타이머 시작 (60초)", key="btn_warmup"):
    run_timer("② 준비운동", 60)


# ==========================================
# ③ 본운동 1 섹션
# ==========================================
str.write("---")
str.subheader("③ 본운동 1️⃣: Hook lying + 필라테스 링 드로우-인")
str.caption("💪 도구: 필라테스 링 | 🔄 횟수: 4회 / 1세트")
str.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQBnFe0M5_wS1ZawgpO_WIp9sNH0KEh59PSQ&s", caption="Hook lying 드로우-인 동작 가이드 [출처: 자체 제작 AI 시각자료]")
str.success("**🏃 수행 방법**\n\n갈고리 누운 자세에서 무릎 사이에 필라테스 링을 위치시키고, 숨을 내쉬며 링을 조임과 동시에 배꼽을 척추 쪽으로 당깁니다.")
str.error("**🔍 파트너 체크리스트**\n\n허리가 과도하게 바닥을 누르거나 꺾이지 않는지, 엉덩이 근육이 과개입하지 않는지 확인하세요.")

# ⏱️ 본운동 1 전용 타이머 배치
if str.button("⏱️ 본운동 1️⃣ 타이머 시작 (60초)", key="btn_main1"):
    run_timer("③ 본운동 1️⃣", 60)


# ==========================================
# ③ 본운동 2 섹션
# ==========================================
str.write("---")
str.subheader("③ 본운동 2️⃣: 런지 + 세라밴드 PNF 패턴")
str.caption("💪 도구: 세라밴드 | 🔄 횟수: 좌우 각 4회 / 1세트")
str.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_yoHwwy8Uc2d4LzhWXHldtNyhwSkLgNPFfw&s", caption="미니 런지 + 세라밴드 PNF 동작 가이드 [출처: 자체 제작 AI 시각자료]")
str.success("**🏃 수행 방법**\n\n무릎 각도를 45°~60°(미니 런지)로 설정하여 골반 중립을 유지합니다. 복부 브레이싱을 잡은 채 세라밴드를 대각선 상방 패턴으로 당깁니다.")
str.error("**🔍 파트너 체크리스트**\n\n대각선 저항을 주는 동안 환자의 요추가 과전만되거나 무릎 정렬이 깨지지 않는지 확인하세요.")

# ⏱️ 본운동 2 전용 타이머 배치
if str.button("⏱️ 본운동 2️⃣ 타이머 시작 (90초)", key="btn_main2"):
    run_timer("③ 본운동 2️⃣", 90)


# ==========================================
# ③ 본운동 3 섹션
# ==========================================
str.write("---")
str.subheader("③ 본운동 3️⃣: 시각 반응형 이중과제 교란 훈련")
str.caption("💪 도구: 필라테스 링 | 🔄 횟수: 무작위 총 6회 / 1세트")
str.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSF57QUYX1LtsaLGyZ6lPilQbF7GWsCFa5ZAw&s", caption="이중과제 동작 가이드 [출처: 자체 제작 AI 시각자료]")
str.success("**<b>🏃 수행 방법</b>**\n\n와이드 스쿼트 자세로 하체를 단단히 고정하고 링을 가슴 앞에 쥡니다. 파트너가 전방에서 무작위로 손을 뻗으면 흉추를 회전해 링 안으로 조준합니다.")
str.error("**🔍 파트너 체크리스트**\n\n손을 뻗는 순간 요추에서 회전이나 미끄러지는 전단력이 발생하지 않는지 모니터링합니다.")

# ⏱️ 본운동 3 전용 타이머 배치
if str.button("⏱️ 본운동 3️⃣ 타이머 시작 (90초)", key="btn_main3"):
    run_timer("③ 본운동 3️⃣", 90)


# ==========================================
# ④ 마무리운동 섹션
# ==========================================
str.write("---")
str.subheader("④ 마무리운동: Standing Roll Down & Up with Ring")
str.caption("💪 도구: 필라테스 링 | 🔄 횟수: 1회")
str.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSF57QUYX1LtsaLGyZ6lPilQbF7GWsCFa5ZAw&s", caption="마무리 롤 업 앤 다운 동작 가이드 [출처: 자체 제작 AI 시각자료]")
str.success("**🏃 수행 방법**\n\n선 자세에서 숨을 내쉬며 머리→등→허리 순으로 말아 내려갑니다. 올라올 때는 링을 조이는 힘을 주며 아랫배를 당겨 척추를 하나씩 쌓아 올립니다.")
str.error("**🔍 파트너 체크리스트**\n\n옆에서 관찰하며 환자가 올라올 때 링을 조이는 힘 덕분에 요추 불안정성 분절이 흔들리지 않는지 확인합니다.")

# ⏱️ 마무리운동 전용 타이머 배치
if str.button("⏱️ 마무리운동 타이머 시작 (60초)", key="btn_finish"):
    run_timer("④ 마무리운동", 60)
