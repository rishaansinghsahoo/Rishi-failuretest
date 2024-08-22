import streamlit as st

st.title("Rishi failure test")
q=[1,2,3,4,5,6,7,8]

for c in q:
    st.write(c)
    with st.form(str(c)):
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
    
