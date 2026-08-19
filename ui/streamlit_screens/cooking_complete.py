"""⑪ 조리 완성 화면 - 마지막 단계까지 끝냈을 때 보여주는 축하 화면.

등록 흐름의 '저장이 완료됐어요!'(complete.py, FR-08 원본 보존/user_custom 저장)와는 다른
화면이다 - 여기는 표준/대체 레시피를 따라 조리를 끝냈다는 확인일 뿐, 별도 저장 동작은 없다.
"""
import streamlit as st

from nav import goto
from theme import ICON_CHECK_CIRCLE, render_spacer


def render() -> None:
    recipe = st.session_state.get("recipe") or {}
    dish_name = recipe.get("dish_name", "오늘의 요리")
    total_minutes = sum(step.get("minutes", 0) for step in recipe.get("steps", []))

    render_spacer()
    st.markdown(f'<div class="ce-lead-icon positive">{ICON_CHECK_CIRCLE}</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="ce-center"><h1>요리가 완성됐어요!</h1>'
        f"<p>{dish_name}, 맛있게 완성했어요. 수고하셨어요!</p></div>",
        unsafe_allow_html=True,
    )

    if total_minutes:
        st.markdown(
            f'<div style="text-align:center;"><span class="ce-status-badge">'
            f"총 조리 시간 약 {total_minutes}분</span></div>",
            unsafe_allow_html=True,
        )

    render_spacer()

    if st.button("처음 화면으로", type="primary", use_container_width=True):
        st.session_state.recipe = None
        st.session_state.pending_recipe_key = None
        st.session_state.chat_log = []
        st.session_state.substituted_ingredient = None
        st.session_state.step_number = 1
        goto("start")
