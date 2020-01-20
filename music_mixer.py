import sys
from utils import Helper


class MusicMixer:
    def __init__(self, existing_playlist_file, changes_file, output_file):
        self.music_data = Helper.read_input(existing_playlist_file)
        self.changes = Helper.read_input(changes_file)
        self.output_file = output_file

    '''
    Dispatcher method
    '''
    def perform_change_action(self, action, **kwargs):
        unknown_action = lambda: self.raise_(Exception("Action not supported"))
        func = getattr(self, action, lambda: unknown_action)
        return func(**kwargs)

    def raise_(self, ex):
        raise ex

    def mix_playlist(self):
        for change in self.changes:
            self.perform_change_action(action=change['action'], change=change)
        Helper.write_output(self.output_file, self.music_data)

    def add_song(self, change):
        # filter out user from users list
        user_data = self.__filter_user(change=change)
        # filter out playlist from user's collection of play-lists
        play_list = self.__filter_playlist(change=change, user_data=user_data)
        if change['song'] in self.music_data['songs']:
            # check if song already in playlist before appending
            if change['song'] not in play_list['songs']:
                play_list['songs'].append(change['song'])
        else:
            raise Exception('Unknown song. This function only adds an existing songs to an existing playlist')

    def __filter_user(self, change):
        user_data = [user for user in self.music_data['users'] if user['name'] == change['user']]
        if len(user_data) == 0:
            raise Exception("User not found")
        if len(user_data) != 1:
            raise Exception("More than one user found")
        return user_data[0]

    def __filter_playlist(self, change, user_data):
        play_list = [pl for pl in user_data['play-lists'] if pl['name'] == change['playlist-name']]
        if len(play_list) == 0:
            raise Exception("Playlist not found")
        if len(play_list) != 1:
            raise Exception("More than one playlist found")
        return play_list[0]

    def add_playlist(self, change):     # adds a new playlist to existing user
        # filter out user from users list
        user_data = self.__filter_user(change=change)
        new_songs = change['playlist']['songs']
        # appended new playlist
        if change['playlist'] not in user_data['play-lists']:
            user_data['play-lists'].append(change['playlist'])
        self.music_data['songs'].extend(song for song in new_songs if song not in self.music_data['songs'])

    def remove_playlist(self, change):
        # filter out user from users list
        user_data = self.__filter_user(change=change)
        # filter out playlist from user's collection of play-lists
        play_list = self.__filter_playlist(change=change, user_data=user_data)
        # remove playlist
        user_data['play-lists'].remove(play_list)


if __name__ == '__main__':
    # reading cli args
    if len(sys.argv) != 4:
        print("Missing necessary cli arguments")
    else:
        mixer = MusicMixer(sys.argv[1], sys.argv[2], sys.argv[3])
        mixer.mix_playlist()
