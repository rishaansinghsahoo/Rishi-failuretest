import streamlit as st

st.title("Rishi failure test")

with st.form("question 1"):
    n1=9045
    n2=1043
    s=n1+n2
    st.write( "what is the sum of ",n1,"&",n2)
    a=st.number_input("enter your answer",step=1)
    if st.form_submit_button("check answer"):
        st.write("your answer:",a)
        st.write("actual answer:",s)
        if a==s:
            st.write("yay you are cooooooooorrrrrrrrrrrreeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccct")
        else:
            st.write("you get a reeeeeeeeeeeeeeeeeeeeeeeeeedddddddddddddddddddddddddddddddddd caaaaaaaaaaaaarrrrrrrd booooooooooo")
