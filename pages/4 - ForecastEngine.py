column1, column2, column3, column4, column5 = st.columns([1, 1, 1, 2 , 1])
with column1:
    st.image(ytube, '[Ledgr\'s YouTube Channel](%s)' % url_ytube)
with column2:
    st.image(fbook, '[Ledgr\'s FaceBook Page ](%s)' % url_fb)
with column3:
    st.image(linkedin,  '[Our LinkedIn Page ](%s)' % url_linkedin)
with column4:
    st.write(" ")
    st.image(ledgrblog,  '[Ledgr\'s Blog ](%s)' % url_blog)
    st.write(" ")
with column5:
    st.image(insta,  '[Ledgr\'s @ Instagram ](%s)' % url_insta)
