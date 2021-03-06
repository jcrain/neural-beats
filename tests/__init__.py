from mido import Message, MetaMessage, MidiFile, MidiTrack

# MIDI test objects

# Track that is already quantized.
track0 = MidiTrack()
track0.append(MetaMessage('track_name', name='test0', time=0))
track0.append(Message('note_on', note=60, velocity=64, time=0))
track0.append(Message('note_off', note=60, velocity=64, time=50))
track0.append(MetaMessage('end_of_track', time=0))

# Simple track that is not quantized.
track1 = MidiTrack()
track1.append(MetaMessage('track_name', name='test1', time=0))
track1.append(Message('note_on', note=60, velocity=64, time=2))
track1.append(Message('note_off', note=60, velocity=64, time=50))
track1.append(MetaMessage('end_of_track', time=0))

# Track with notes that, when quantized to 32nd notes, would run over
# the original end time of the track.
track2 = MidiTrack()
track2.append(MetaMessage('track_name', name='test2', time=0))
track2.append(Message('note_on', note=60, velocity=64, time=29))
track2.append(Message('note_off', note=60, velocity=64, time=31))
track2.append(MetaMessage('end_of_track', time=0))

meta_track = MidiTrack()
meta_track.append(MetaMessage('track_name', name='meta-track', time=0))
midi_notes_in_track0 = MidiFile()
midi_notes_in_track0.tracks.append(track0)

midi_notes_in_track1 = MidiFile()
midi_notes_in_track1.tracks.append(meta_track)
midi_notes_in_track1.tracks.append(track0)
