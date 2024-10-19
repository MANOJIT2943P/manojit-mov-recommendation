import streamlit as st
import pickle
import gzip

movies=pickle.load(open("movieList.pkl","rb"))
with gzip.open("similarity.pkl.gz",'rb') as f:
    similarity=pickle.load(f)

movie_list=movies['title'].values

st.header("Movie Recommendation System")
val=st.selectbox("Select Movie",movie_list)
limit=st.slider("Enter Suggestion limit",1,50)
st.caption("limit should be less than equal to 50")




#recommendation function
def recommend(movie):
    index=movies[movies['title']==movie].index[0]

    distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector:vector[1])

    recommended_movie=[]
    # recommended_poster=[]

    for i in distance[1:limit+1]:
        recommended_movie.append(movies.iloc[i[0]].title)

    return recommended_movie #,recommended_poster

if st.button("Recommend"):
    movie_name=recommend(val)
    
    st.subheader("Top {} Suggestions are".format(limit))
    con=st.container()
    
    
    for i in range(len(movie_name)):
        prompt="{}. {}".format(i+1,movie_name[i])
        url="https://www.google.com/search?q={} + movie".format(movie_name[i])
        con.link_button(prompt,url)
        
        
