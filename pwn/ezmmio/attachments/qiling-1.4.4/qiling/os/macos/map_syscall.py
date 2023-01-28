#!/usr/bin/env python3
#
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#

from qiling.const import QL_ARCH
from qiling.os.posix.posix import SYSCALL_PREF

def get_syscall_mapper(archtype: QL_ARCH):
    syscall_table = {
        QL_ARCH.X8664 : x8664_syscall_table,
        QL_ARCH.ARM64 : arm64_syscall_table
    }[archtype]

    syscall_fixup = {
        QL_ARCH.X8664 : lambda n: (n - 0x2000000) if 0x2000000 <= n <= 0x3000000 else n,
        QL_ARCH.ARM64 : lambda n: (n - 0xffffffffffffff00) if n >= 0xffffffffffffff00 else n
    }[archtype]

    def __mapper(syscall_num: int) -> str:
        return f'{SYSCALL_PREF}{syscall_table[syscall_fixup(syscall_num)]}'

    return __mapper


arm64_syscall_table = {
    1: 'exit',
    2: 'fork',
    3: 'read',
    4: 'write',
    5: 'open',
    6: 'close',
    7: 'wait4',
    10: 'unlink',
    12: 'chdir',
    15: 'chmod',
    25: 'geteuid',
    27: 'recvmsg',
    28: 'sendmsg',
    29: 'recvfrom',
    30: 'accept',
    31: 'getpeername',
    32: 'getsockname',
    33: 'access_macos',
    34: 'chflags',
    35: 'fchflags',
    36: 'semaphore_wait_signal_trap',
    37: 'kill',
    38: 'semaphore_timedwait_signal_trap',
    39: 'getppid',
    40: 'kernelrpc_mach_port_guard_trap',
    41: 'kernelrpc_mach_port_unguard_trap',
    43: 'getegid',
    44: 'task_for_pid',
    45: 'pid_for_task',
    46: 'sigaction',
    47: 'getgid',
    48: 'macx_swapoff',
    49: 'getlogin',
    50: 'setlogin',
    51: 'acct',
    52: 'macx_backing_store_recovery',
    53: 'sigaltstack',
    54: 'ioctl',
    55: 'reboot',
    56: 'revoke',
    57: 'symlink',
    58: 'readlink',
    59: 'execve',
    60: 'syscall_thread_switch',
    61: 'chroot',
    65: 'msync',
    73: 'munmap',
    74: 'mprotect',
    75: 'madvise',
    78: 'mincore',
    79: 'getgroups',
    80: 'setgroups',
    81: 'getpgrp',
    82: 'setpgid',
    83: 'setitimer',
    85: 'swapon',
    86: 'getitimer',
    88: 'mach_timebase_info',
    89: 'getdtablesize',
    90: 'dup2',
    91: 'mk_timer_destroy',
    92: 'fcntl64_macos',
    93: 'select',
    95: 'fsync',
    96: 'setpriority',
    97: 'socket',
    98: 'connect',
    100: 'getpriority',
    104: 'bind',
    105: 'setsockopt',
    106: 'listen',
    111: 'sigsuspend',
    117: 'getrusage',
    118: 'getsockopt',
    120: 'readv',
    121: 'writev',
    122: 'settimeofday',
    123: 'fchown',
    124: 'fchmod',
    126: 'setreuid',
    127: 'setregid',
    128: 'rename',
    131: 'flock',
    132: 'mkfifo',
    133: 'sendto',
    134: 'shutdown',
    135: 'socketpair',
    136: 'mkdir',
    137: 'rmdir',
    138: 'utimes',
    139: 'futimes',
    140: 'adjtime',
    142: 'gethostuuid',
    147: 'setsid',
    148: 'setquota',
    149: 'quota',
    151: 'getpgid',
    152: 'setprivexec',
    153: 'pread',
    154: 'pwrite',
    155: 'nfssvc',
    159: 'unmount',
    161: 'getfh',
    165: 'quotactl',
    167: 'mount',
    169: 'csops',
    170: 'csops_audittoken',
    173: 'waitid',
    178: 'kdebug_trace_string',
    179: 'kdebug_trace64',
    180: 'kdebug_trace',
    181: 'setgid',
    182: 'setegid',
    183: 'seteuid',
    184: 'sigreturn',
    185: 'chud',
    187: 'fdatasync',
    191: 'pathconf',
    192: 'fpathconf',
    194: 'getrlimit',
    195: 'setrlimit',
    196: 'getdirentries',
    197: 'mmap2',
    199: 'lseek',
    200: 'truncate',
    201: 'ftruncate',
    202: 'sysctl',
    203: 'mlock',
    204: 'munlock',
    205: 'undelete',
    216: 'open_dprotected_np',
    220: 'getattrlist',
    221: 'setattrlist',
    222: 'getdirentriesattr',
    223: 'exchangedata',
    225: 'searchfs',
    226: 'delete',
    227: 'copyfile',
    228: 'fgetattrlist',
    229: 'fsetattrlist',
    230: 'poll',
    231: 'watchevent',
    232: 'waitevent',
    233: 'modwatch',
    234: 'getxattr',
    235: 'fgetxattr',
    236: 'setxattr',
    237: 'fsetxattr',
    238: 'removexattr',
    239: 'fremovexattr',
    240: 'listxattr',
    241: 'flistxattr',
    242: 'fsctl',
    243: 'initgroups',
    244: 'posix_spawn',
    245: 'ffsctl',
    247: 'nfsclnt',
    248: 'fhopen',
    250: 'minherit',
    251: 'semsys',
    252: 'msgsys',
    253: 'shmsys',
    254: 'semctl',
    255: 'semget',
    256: 'semop',
    258: 'msgctl',
    259: 'msgget',
    260: 'msgsnd',
    261: 'msgrcv',
    262: 'shmat',
    263: 'shmctl',
    264: 'shmdt',
    265: 'shmget',
    266: 'shm_open',
    267: 'shm_unlink',
    268: 'sem_open',
    269: 'sem_close',
    270: 'sem_unlink',
    271: 'sem_wait',
    272: 'sem_trywait',
    273: 'sem_post',
    274: 'sysctlbyname',
    277: 'open_extended',
    278: 'umask_extended',
    279: 'stat_extended',
    280: 'lstat_extended',
    281: 'fstat_extended',
    282: 'chmod_extended',
    283: 'fchmod_extended',
    284: 'access_extended',
    285: 'settid',
    286: 'gettid',
    287: 'setsgroups',
    288: 'getsgroups',
    289: 'setwgroups',
    290: 'getwgroups',
    291: 'mkfifo_extended',
    292: 'mkdir_extended',
    293: 'identitysvc',
    294: 'shared_region_check_np',
    296: 'vm_pressure_monitor',
    297: 'psynch_rw_longrdlock',
    298: 'psynch_rw_yieldwrlock',
    299: 'psynch_rw_downgrade',
    300: 'psynch_rw_upgrade',
    301: 'psynch_mutexwait',
    302: 'psynch_mutexdrop',
    303: 'psynch_cvbroad',
    304: 'psynch_cvsignal',
    305: 'psynch_cvwait',
    306: 'psynch_rw_rdlock',
    307: 'psynch_rw_wrlock',
    308: 'psynch_rw_unlock',
    309: 'psynch_rw_unlock2',
    310: 'getsid',
    311: 'settid_with_pid',
    312: 'psynch_cvclrprepost',
    313: 'aio_fsync',
    314: 'aio_return',
    315: 'aio_suspend',
    316: 'aio_cancel',
    317: 'aio_error',
    318: 'aio_read',
    319: 'aio_write',
    320: 'lio_listio',
    322: 'iopolicysys',
    323: 'process_policy',
    324: 'mlockall',
    325: 'munlockall',
    327: 'issetugid',
    328: 'pthread_kill',
    329: 'pthread_sigmask',
    330: 'sigwait',
    331: 'disable_threadsignal',
    332: 'pthread_markcancel',
    333: 'pthread_canceled',
    334: 'semwait_signal',
    336: 'proc_info',
    337: 'sendfile',
    338: 'stat',
    339: 'fstat',
    340: 'lstat',
    341: 'stat64_extended',
    342: 'lstat64_extended',
    343: 'fstat64_extended',
    344: 'getdirentries64',
    345: 'statfs',
    346: 'fstatfs',
    347: 'getfsstat',
    348: 'pthread_chdir',
    349: 'pthread_fchdir',
    350: 'audit',
    351: 'auditon',
    353: 'getauid',
    354: 'setauid',
    357: 'getaudit_addr',
    358: 'setaudit_addr',
    359: 'auditctl',
    360: 'bsdthread_create',
    361: 'bsdthread_terminate',
    362: 'kqueue',
    363: 'kevent',
    364: 'lchown',
    365: 'stack_snapshot',
    366: 'bsdthread_register',
    367: 'workq_open',
    368: 'workq_kernreturn',
    369: 'kevent64',
    370: 'old_semwait_signal',
    371: 'old_semwait_signal_nocancel',
    372: 'thread_selfid',
    373: 'ledger',
    374: 'kevent_qos',
    380: 'mac_execve',
    381: 'mac_syscall',
    382: 'mac_get_file',
    383: 'mac_set_file',
    384: 'mac_get_link',
    385: 'mac_set_link',
    386: 'mac_get_proc',
    387: 'mac_set_proc',
    388: 'mac_get_fd',
    389: 'mac_set_fd',
    390: 'mac_get_pid',
    396: 'read_nocancel',
    397: 'write_nocancel',
    398: 'open_nocancel',
    399: 'close_nocancel',
    400: 'wait4_nocancel',
    401: 'recvmsg_nocancel',
    402: 'sendmsg_nocancel',
    403: 'recvfrom_nocancel',
    404: 'accept_nocancel',
    405: 'msync_nocancel',
    406: 'fcntl_nocancel',
    407: 'select_nocancel',
    408: 'fsync_nocancel',
    409: 'connect_nocancel',
    410: 'sigsuspend_nocancel',
    411: 'readv_nocancel',
    412: 'writev_nocancel',
    413: 'sendto_nocancel',
    414: 'pread_nocancel',
    415: 'pwrite_nocancel',
    416: 'waitid_nocancel',
    417: 'poll_nocancel',
    418: 'msgsnd_nocancel',
    419: 'msgrcv_nocancel',
    420: 'sem_wait_nocancel',
    421: 'aio_suspend_nocancel',
    422: 'sigwait_nocancel',
    423: 'semwait_signal_nocancel',
    424: 'mac_mount',
    425: 'mac_get_mount',
    426: 'mac_getfsstat',
    427: 'fsgetpath',
    428: 'audit_session_self',
    429: 'audit_session_join',
    430: 'fileport_makeport',
    431: 'fileport_makefd',
    432: 'audit_session_port',
    433: 'pid_suspend',
    434: 'pid_resume',
    435: 'pid_hibernate',
    436: 'pid_shutdown_sockets',
    438: 'shared_region_map_and_slide_np',
    439: 'kas_info',
    440: 'memorystatus_control',
    441: 'guarded_open_np',
    442: 'guarded_close_np',
    443: 'guarded_kqueue_np',
    444: 'change_fdguard_np',
    446: 'proc_rlimit_control',
    447: 'connectx',
    448: 'disconnectx',
    449: 'peeloff',
    450: 'socket_delegate',
    451: 'telemetry',
    452: 'proc_uuid_policy',
    453: 'memorystatus_get_level',
    454: 'system_override',
    455: 'vfs_purge',
    456: 'sfi_ctl',
    457: 'sfi_pidctl',
    458: 'coalition',
    459: 'coalition_info',
    460: 'necp_match_policy',
    461: 'getattrlistbulk',
    463: 'openat',
    464: 'openat_nocancel',
    465: 'renameat',
    466: 'faccessat',
    467: 'fchmodat',
    468: 'fchownat',
    470: 'fstatat',
    471: 'linkat',
    472: 'unlinkat',
    473: 'readlinkat',
    474: 'symlinkat',
    475: 'mkdirat',
    476: 'getattrlistat',
    477: 'proc_trace_log',
    478: 'bsdthread_ctl',
    479: 'openbyid_np',
    480: 'recvmsg_x',
    481: 'sendmsg_x',
    482: 'thread_selfusage',
    483: 'csrctl',
    484: 'guarded_open_dprotected_np',
    485: 'guarded_write_np',
    486: 'guarded_pwrite_np',
    487: 'guarded_writev_np',
    488: 'rename_ext',
    489: 'mremap_encrypted',
    490: 'netagent_trigger',
    491: 'stack_snapshot_with_config',
    492: 'microstackshot',
    493: 'grab_pgo_data',
    499: 'work_interval_ctl',
}

x8664_syscall_table = {
    1: 'exit',
    2: 'fork',
    3: 'read',
    4: 'write',
    5: 'open',
    6: 'close',
    7: 'wait4',
    9: 'link',
    10: 'unlink',
    12: 'chdir',
    13: 'fchdir',
    14: 'mknod',
    15: 'chmod',
    16: 'chown',
    18: 'getfsstat',
    20: 'getpid',
    23: 'setuid',
    24: 'getuid',
    25: 'geteuid',
    26: 'ptrace',
    27: 'recvmsg',
    28: 'sendmsg',
    29: 'recvfrom',
    30: 'accept',
    31: 'getpeername',
    32: 'getsockname',
    33: 'access_macos',
    34: 'chflags',
    35: 'fchflags',
    36: 'sync',
    37: 'kill',
    39: 'getppid',
    41: 'dup',
    42: 'pipe',
    43: 'getegid',
    44: 'profil',
    46: 'sigaction',
    47: 'getgid',
    48: 'sigprocmask',
    49: 'getlogin',
    50: 'setlogin',
    51: 'acct',
    52: 'sigpending',
    53: 'sigaltstack',
    54: 'ioctl',
    55: 'reboot',
    56: 'revoke',
    57: 'symlink',
    58: 'readlink',
    59: 'execve',
    60: 'umask',
    61: 'chroot',
    65: 'msync',
    66: 'vfork',
    73: 'munmap',
    74: 'mprotect',
    75: 'madvise',
    78: 'mincore',
    79: 'getgroups',
    80: 'setgroups',
    81: 'getpgrp',
    82: 'setpgid',
    83: 'setitimer',
    86: 'getitimer',
    89: 'getdtablesize',
    90: 'dup2',
    92: 'fcntl64_macos',
    93: 'select',
    95: 'fsync',
    96: 'setpriority',
    97: 'socket',
    98: 'connect',
    100: 'getpriority',
    104: 'bind',
    105: 'setsockopt',
    106: 'listen',
    111: 'sigsuspend',
    116: 'gettimeofday',
    117: 'getrusage',
    118: 'getsockopt',
    120: 'readv',
    121: 'writev',
    122: 'settimeofday',
    123: 'fchown',
    124: 'fchmod',
    126: 'setreuid',
    127: 'setregid',
    128: 'rename',
    131: 'flock',
    132: 'mkfifo',
    133: 'sendto',
    134: 'shutdown',
    135: 'socketpair',
    136: 'mkdir',
    137: 'rmdir',
    138: 'utimes',
    139: 'futimes',
    140: 'adjtime',
    142: 'gethostuuid',
    147: 'setsid',
    151: 'getpgid',
    152: 'setprivexec',
    153: 'pread',
    154: 'pwrite',
    155: 'nfssvc',
    157: 'statfs',
    158: 'fstatfs',
    159: 'unmount',
    161: 'getfh',
    165: 'quotactl',
    167: 'mount',
    169: 'csops',
    173: 'waitid',
    176: 'add_profil',
    181: 'setgid',
    182: 'setegid',
    183: 'seteuid',
    184: 'sigreturn',
    187: 'fdatasync',
    188: 'stat',
    189: 'fstat',
    190: 'lstat',
    191: 'pathconf',
    192: 'fpathconf',
    194: 'getrlimit',
    195: 'setrlimit',
    196: 'getdirentries',
    197: 'mmap2',
    199: 'lseek',
    200: 'truncate',
    201: 'ftruncate',
    202: 'sysctl',
    203: 'mlock',
    204: 'munlock',
    205: 'undelete',
    206: 'ATsocket',
    207: 'ATgetmsg',
    208: 'ATputmsg',
    209: 'ATPsndreq',
    210: 'ATPsndrsp',
    211: 'ATPgetreq',
    212: 'ATPgetrsp',
    216: 'mkcomplex',
    217: 'statv',
    218: 'lstatv',
    219: 'fstatv',
    220: 'getattrlist',
    221: 'setattrlist',
    222: 'getdirentriesattr',
    223: 'exchangedata',
    224: 'int',
    225: 'searchfs',
    226: 'delete',
    227: 'copyfile',
    228: 'fgetattrlist',
    229: 'fsetattrlist',
    230: 'poll',
    231: 'watchevent',
    232: 'waitevent',
    233: 'modwatch',
    234: 'getxattr',
    235: 'fgetxattr',
    236: 'setxattr',
    237: 'fsetxattr',
    238: 'removexattr',
    239: 'fremovexattr',
    240: 'listxattr',
    241: 'flistxattr',
    242: 'fsctl',
    243: 'initgroups',
    244: 'posix_spawn',
    245: 'ffsctl',
    247: 'nfsclnt',
    248: 'fhopen',
    250: 'minherit',
    251: 'semsys',
    252: 'msgsys',
    253: 'shmsys',
    254: 'semctl',
    255: 'semget',
    256: 'semop',
    258: 'msgctl',
    259: 'msgget',
    260: 'msgsnd',
    261: 'msgrcv',
    262: 'shmat',
    263: 'shmctl',
    264: 'shmdt',
    265: 'shmget',
    266: 'shm_open',
    267: 'shm_unlink',
    268: 'sem_open',
    269: 'sem_close',
    270: 'sem_unlink',
    271: 'sem_wait',
    272: 'sem_trywait',
    273: 'sem_post',
    274: 'sem_getvalue',
    275: 'sem_init',
    276: 'sem_destroy',
    277: 'open_extended',
    278: 'umask_extended',
    279: 'stat_extended',
    280: 'lstat_extended',
    281: 'fstat_extended',
    282: 'chmod_extended',
    283: 'fchmod_extended',
    284: 'access_extended',
    285: 'settid',
    286: 'gettid',
    287: 'setsgroups',
    288: 'getsgroups',
    289: 'setwgroups',
    290: 'getwgroups',
    291: 'mkfifo_extended',
    292: 'mkdir_extended',
    293: 'identitysvc',
    294: 'shared_region_check_np',
    295: 'shared_region_map_np',
    296: 'vm_pressure_monitor',
    297: 'psynch_rw_longrdlock',
    298: 'psynch_rw_yieldwrlock',
    299: 'psynch_rw_downgrade',
    300: 'psynch_rw_upgrade',
    301: 'psynch_mutexwait',
    302: 'psynch_mutexdrop',
    303: 'psynch_cvbroad',
    304: 'psynch_cvsignal',
    305: 'psynch_cvwait',
    306: 'psynch_rw_rdlock',
    307: 'psynch_rw_wrlock',
    308: 'psynch_rw_unlock',
    309: 'psynch_rw_unlock2',
    310: 'getsid',
    311: 'settid_with_pid',
    313: 'aio_fsync',
    314: 'user_ssize_t',
    315: 'aio_suspend',
    316: 'aio_cancel',
    317: 'aio_error',
    318: 'aio_read',
    319: 'aio_write',
    320: 'lio_listio',
    322: 'iopolicysys',
    324: 'mlockall',
    325: 'munlockall',
    327: 'issetugid',
    328: 'pthread_kill',
    329: 'pthread_sigmask',
    330: 'sigwait',
    331: 'disable_threadsignal',
    332: 'pthread_markcancel',
    333: 'pthread_canceled',
    334: 'semwait_signal',
    336: 'proc_info',
    337: 'sendfile',
    338: 'stat64',
    339: 'fstat64',
    340: 'lstat64',
    341: 'stat64_extended',
    342: 'lstat64_extended',
    343: 'fstat64_extended',
    344: 'getdirentries64',
    345: 'statfs64',
    346: 'fstatfs64',
    347: 'getfsstat64',
    348: 'pthread_chdir',
    349: 'pthread_fchdir',
    350: 'audit',
    351: 'auditon',
    353: 'getauid',
    354: 'setauid',
    355: 'getaudit',
    356: 'setaudit',
    357: 'getaudit_addr',
    358: 'setaudit_addr',
    359: 'auditctl',
    360: 'bsdthread_create',
    361: 'bsdthread_terminate',
    362: 'kqueue',
    363: 'kevent',
    364: 'lchown',
    365: 'stack_snapshot',
    366: 'bsdthread_register',
    367: 'workq_open',
    368: 'workq_kernreturn',
    369: 'kevent64',
    370: 'old_semwait_signal',
    371: 'old_semwait_signal_nocancel',
    372: 'thread_selfid',
    379: 'nosys',
    380: 'mac_execve',
    381: 'mac_syscall',
    382: 'mac_get_file',
    383: 'mac_set_file',
    384: 'mac_get_link',
    385: 'mac_set_link',
    386: 'mac_get_proc',
    387: 'mac_set_proc',
    388: 'mac_get_fd',
    389: 'mac_set_fd',
    390: 'mac_get_pid',
    391: 'mac_get_lcid',
    392: 'mac_get_lctx',
    393: 'mac_set_lctx',
    394: 'setlcid',
    395: 'getlcid',
    396: 'read_nocancel',
    397: 'write_nocancel',
    398: 'open_nocancel',
    399: 'close_nocancel',
    400: 'wait4_nocancel',
    401: 'recvmsg_nocancel',
    402: 'sendmsg_nocancel',
    403: 'recvfrom_nocancel',
    404: 'accept_nocancel',
    405: 'msync_nocancel',
    406: 'fcntl_nocancel',
    407: 'select_nocancel',
    408: 'fsync_nocancel',
    409: 'connect_nocancel',
    410: 'sigsuspend_nocancel',
    411: 'readv_nocancel',
    412: 'writev_nocancel',
    413: 'sendto_nocancel',
    414: 'pread_nocancel',
    415: 'pwrite_nocancel',
    416: 'waitid_nocancel',
    417: 'poll_nocancel',
    418: 'msgsnd_nocancel',
    419: 'msgrcv_nocancel',
    420: 'sem_wait_nocancel',
    421: 'aio_suspend_nocancel',
    422: 'sigwait_nocancel',
    423: 'semwait_signal_nocancel',
    424: 'mac_mount',
    425: 'mac_get_mount',
    426: 'mac_getfsstat',
    427: 'fsgetpath',
    428: 'audit_session_self',
    429: 'audit_session_join',
    483: 'csrctl',
    500: 'getentropy',
    520: 'terminate_with_payload',
    521: 'abort_with_payload',
    0x100000a: 'kernelrpc_mach_vm_allocate_trap',
    0x100000c: 'kernelrpc_mach_vm_deallocate_trap',
    0x100000f: 'kernelrpc_mach_vm_map_trap',
    0x1000012: 'kernelrpc_mach_port_deallocate_trap',
    0x1000013: 'kernelrpc_mach_port_mod_refs_trap',
    0x1000018: 'kernelrpc_mach_port_construct_trap',
    0x100001a: 'mach_reply_port',
    0x100001b: 'thread_self_trap',
    0x100001c: 'task_self_trap',
    0x100001d: 'host_self_trap',
    0x100001f: 'mach_msg_trap',
    0x3000003: 'thread_fast_set_cthread_self64',
}