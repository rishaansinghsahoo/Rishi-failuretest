import streamlit as st

st.title("Rishi failure test")
q=[1,2,3,4,5,6,7,8]
list1=[908034343262604,6650034326536,4487546390020,454353740,5765463550,5353432820,5598436290,985544271818118800950]
list2=[65654644637543,3425543262818541,4425446289180,3321000101010364536927902,6643425273649489499393434,7705169,5409310006,109999005425252522141111230000000]
st.write(list1[3])
i=0
for c in q:
    st.write(i)
    with st.form(str(c)):
        n1=list1[i]
        n2=list2[i]
        i=i+1
        s=n1+n2
        st.write("what is the sum of ",n1,"&",n2)
        st.write(n1)
        st.write("&")
        st.write(n2)
        a=st.number_input("enter your answer",step=1)
        if st.form_submit_button("check answer"):
            st.write("your answer:",a)
            st.write("actual answer:",s)
            if a==s:
                st.write("yay you are cooooooooorrrrrrrrrrrreeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccct")
            else:
                st.write("you get a reeeeeeeeeeeeeeeeeeeeeeeeeedddddddddddddddddddddddddddddddddd caaaaaaaaaaaaarrrrrrrd booooooooooo")
    
