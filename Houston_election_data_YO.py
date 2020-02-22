{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "election_file = \"houston_election_data.csv\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "election_file_pd = pd.read_csv(election_file)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Candidate</th>\n",
       "      <th>County</th>\n",
       "      <th>Voter ID</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>Dwight A. Boykins</td>\n",
       "      <td>Harris County</td>\n",
       "      <td>3363684</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>Bill King</td>\n",
       "      <td>Fort Bend County</td>\n",
       "      <td>6114041</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>Sylvester Turner</td>\n",
       "      <td>Fort Bend County</td>\n",
       "      <td>9143483</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>Bill King</td>\n",
       "      <td>Fort Bend County</td>\n",
       "      <td>3122710</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>Sylvester Turner</td>\n",
       "      <td>Montgomery County</td>\n",
       "      <td>6824440</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Candidate             County  Voter ID\n",
       "0  Dwight A. Boykins      Harris County   3363684\n",
       "1          Bill King   Fort Bend County   6114041\n",
       "2   Sylvester Turner   Fort Bend County   9143483\n",
       "3          Bill King   Fort Bend County   3122710\n",
       "4   Sylvester Turner  Montgomery County   6824440"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "election_file_pd.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(241032, 3)"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "election_file_pd.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "Candidates = election_file_pd.groupby('Candidate')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Sylvester Turner        111789\n",
       "Tony Buzbee              69361\n",
       "Bill King                33772\n",
       "Dwight A. Boykins        14212\n",
       "Victoria Romero           2933\n",
       "Sue Lovell                2932\n",
       "Demetria Smith            1694\n",
       "Roy J. Vasquez            1556\n",
       "Kendall Baker              982\n",
       "Derrick Broze              686\n",
       "Naoufal Houjami            560\n",
       "Johnny “J.T.” Taylor       555\n",
       "Name: Candidate, dtype: int64"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "election_file_pd['Candidate'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Sylvester Turner        0.463793\n",
       "Tony Buzbee             0.287767\n",
       "Bill King               0.140114\n",
       "Dwight A. Boykins       0.058963\n",
       "Victoria Romero         0.012169\n",
       "Sue Lovell              0.012164\n",
       "Demetria Smith          0.007028\n",
       "Roy J. Vasquez          0.006456\n",
       "Kendall Baker           0.004074\n",
       "Derrick Broze           0.002846\n",
       "Naoufal Houjami         0.002323\n",
       "Johnny “J.T.” Taylor    0.002303\n",
       "Name: Candidate, dtype: float64"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "election_file_pd['Candidate'].value_counts(normalize=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "votes = election_file_pd['Candidate'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "percent = election_file_pd['Candidate'].value_counts(normalize=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>votes</th>\n",
       "      <th>percent</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>Sylvester Turner</td>\n",
       "      <td>111789</td>\n",
       "      <td>0.463793</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Tony Buzbee</td>\n",
       "      <td>69361</td>\n",
       "      <td>0.287767</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Bill King</td>\n",
       "      <td>33772</td>\n",
       "      <td>0.140114</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Dwight A. Boykins</td>\n",
       "      <td>14212</td>\n",
       "      <td>0.058963</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Victoria Romero</td>\n",
       "      <td>2933</td>\n",
       "      <td>0.012169</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Sue Lovell</td>\n",
       "      <td>2932</td>\n",
       "      <td>0.012164</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Demetria Smith</td>\n",
       "      <td>1694</td>\n",
       "      <td>0.007028</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Roy J. Vasquez</td>\n",
       "      <td>1556</td>\n",
       "      <td>0.006456</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Kendall Baker</td>\n",
       "      <td>982</td>\n",
       "      <td>0.004074</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Derrick Broze</td>\n",
       "      <td>686</td>\n",
       "      <td>0.002846</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Naoufal Houjami</td>\n",
       "      <td>560</td>\n",
       "      <td>0.002323</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Johnny “J.T.” Taylor</td>\n",
       "      <td>555</td>\n",
       "      <td>0.002303</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                       votes   percent\n",
       "Sylvester Turner      111789  0.463793\n",
       "Tony Buzbee            69361  0.287767\n",
       "Bill King              33772  0.140114\n",
       "Dwight A. Boykins      14212  0.058963\n",
       "Victoria Romero         2933  0.012169\n",
       "Sue Lovell              2932  0.012164\n",
       "Demetria Smith          1694  0.007028\n",
       "Roy J. Vasquez          1556  0.006456\n",
       "Kendall Baker            982  0.004074\n",
       "Derrick Broze            686  0.002846\n",
       "Naoufal Houjami          560  0.002323\n",
       "Johnny “J.T.” Taylor     555  0.002303"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.DataFrame({'votes': votes, 'percent': percent})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
