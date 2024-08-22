import streamlit as st

st.title("Rishi failure test")
q=[1,2,3,4,5,6,7,8]
list1=[908004,665006,448720,4540,576540,5320,559890,9800950]
list2=[656543,342541,442180,332902,664434,770569,54310006,9999000000000]
st.write(list1[3])
i=0
for c in q:
    st.write(i)
    with st.form(str(c)):
        n1=list1[i]
        n2=list2[i]
        i=i+1
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
    
