import numpy
import theano
import theano.tensor as T
from app import genre_list, tmdb

rng = numpy.random
N = 0
feats = 0
x = T.matrix("x")
y = T.vector("y")
training_steps = 1000

def get_movie_features(movie):
    genre_vector = numpy.zeros(len(genre_list))

    gl = []
    if movie.has_key('genre_ids'):
        gl = movie['genre_ids']
    else :
        gl = map(lambda x: x['id'], movie['genres'])

    j=0
    for i in range(len(genre_list)):
        if j >= len(gl):
            break
        if genre_list[i] == gl[j]:
            j = j+1
            genre_vector[i]=1

    return genre_vector

def movies_to_vector(movie_infos):
    ret = get_movie_features(movie_infos[0])
    it = iter(movie_infos)
    next(it)

    for m in it: 
        ret = numpy.vstack([ret, get_movie_features(m)])
    return ret

def run(movie_infos, scores):
    movie_features = movies_to_vector(movie_infos)
    print 'movies to feature vectors'
    N,feats = numpy.shape(movie_features)

    w = theano.shared(rng.randn(feats), name="w")
    b = theano.shared(0., name="b")

    prediction = 1 / (1 + T.exp(-T.dot(x, w) - b))
    p_1 = prediction
    xent = -y * T.log(p_1) - (1-y) * T.log(1-p_1) 
    cost = xent.mean() + 0.01 * (w ** 2).sum()
    gw, gb = T.grad(cost, [w, b])             
                                              
    train = theano.function(
                  inputs=[x,y],
                  outputs=[prediction, xent],
                  updates=((w, w - 0.1 * gw), (b, b - 0.1 * gb)))

    predict = theano.function(inputs=[x], outputs=prediction)

    print('training')
    for i in range(training_steps):
        pred, err = train(movie_features, scores)

    print('done')
    print 'popular movies to training vectors'
    popular = tmdb.Movies('popular').info()['results']

    print('done')
    
    ret = predict(movies_to_vector(popular))
    print 'run done'
    return ret

