EDA
================

``` r
suppressPackageStartupMessages(library(tidyverse))
```

    ## Warning: package 'tibble' was built under R version 3.5.2

    ## Warning: package 'purrr' was built under R version 3.5.2

    ## Warning: package 'dplyr' was built under R version 3.5.2

``` r
suppressPackageStartupMessages(library(knitr))
suppressPackageStartupMessages(library(ggplot2))
suppressPackageStartupMessages(library(broom))
suppressPackageStartupMessages(library(ggthemes))
```

``` r
kable(head(smart_survey))
```

| smartphone\_OS | num\_smartphone\_OS | smartphone\_OS\_years | pre\_smartphone\_OS | future\_smartphone\_OS | family\_smartphone\_OS | friend\_smartphone\_OS | PC\_OS | num\_PC\_OS | PC\_OS\_years | future\_PC\_OS | workplace\_PC\_OS     |
| :------------- | ------------------: | --------------------: | :------------------ | :--------------------- | :--------------------- | :--------------------- | :----- | ----------: | ------------: | :------------- | :-------------------- |
| iOS            |                   5 |                     3 | iOS                 | iOS                    | iOS                    | iOS                    | MacOS  |           5 |             1 | iOS            | Either/Doesn’t Matter |
| Android        |                   3 |                     3 | iOS                 | Android                | iOS                    | iOS                    | MacOS  |           4 |             4 | iOS            | Windows               |
| iOS            |                   4 |                     2 | iOS                 | iOS                    | Android                | iOS                    | MacOS  |           4 |             1 | Other          | Mac OS                |
| iOS            |                   3 |                     2 | iOS                 | iOS                    | iOS                    | iOS                    | Other  |           3 |             1 | iOS            | Windows               |
| iOS            |                   4 |                     3 | iOS                 | iOS                    | iOS                    | iOS                    | MacOS  |           3 |             1 | iOS            | Either/Doesn’t Matter |
| Android        |                   3 |                     2 | Android             | Android                | Android                | iOS                    | MacOS  |           5 |             3 | iOS            | Either/Doesn’t Matter |

``` r
sum_stats <- smart_survey %>%
  select(num_smartphone_OS,smartphone_OS_years,num_PC_OS,PC_OS_years) %>%
  summary()

kable(sum_stats)
```

|  | num\_smartphone\_OS | smartphone\_OS\_years |  num\_PC\_OS  | PC\_OS\_years |
|  | :------------------ | :-------------------- | :-----------: | :-----------: |
|  | Min. :2.000         | Min. :1.000           |  Min. :3.000  |  Min. :1.000  |
|  | 1st Qu.:3.500       | 1st Qu.:1.000         | 1st Qu.:4.000 | 1st Qu.:1.000 |
|  | Median :4.000       | Median :2.000         | Median :4.000 | Median :1.000 |
|  | Mean :4.148         | Mean :2.074           |  Mean :4.185  |  Mean :1.963  |
|  | 3rd Qu.:5.000       | 3rd Qu.:3.000         | 3rd Qu.:5.000 | 3rd Qu.:3.000 |
|  | Max. :5.000         | Max. :4.000           |  Max. :5.000  |  Max. :5.000  |

![](eda_viz_files/figure-gfm/unnamed-chunk-4-1.png)<!-- -->

``` r
smart_survey %>%
  filter(smartphone_OS=="iOS") %>%
  ggplot(aes(x=num_smartphone_OS)) +
  geom_bar() +
  ggtitle("Level of satisfaction of iOS users") +
  ylab("") +
  xlab("") +
  expand_limits(x=1) 
```

![](eda_viz_files/figure-gfm/unnamed-chunk-5-1.png)<!-- -->

``` r
smart_survey %>%
  filter(smartphone_OS=="Android") %>%
  ggplot(aes(x=num_smartphone_OS)) +
  geom_bar() +
  ggtitle("Level of satisfaction of Android users") +
  ylab("") +
  xlab("") +
  expand_limits(x=1)
```

![](eda_viz_files/figure-gfm/unnamed-chunk-6-1.png)<!-- -->

![](eda_viz_files/figure-gfm/unnamed-chunk-7-1.png)<!-- -->

![](eda_viz_files/figure-gfm/unnamed-chunk-8-1.png)<!-- -->

``` r
smart_survey %>%
  filter(PC_OS=="MacOS") %>%
  ggplot(aes(x=num_PC_OS)) +
  geom_bar() +
  ggtitle("Level of satisfaction of MacOS users") +
  ylab("") +
  xlab("") +
  expand_limits(x=1)
```

![](eda_viz_files/figure-gfm/unnamed-chunk-9-1.png)<!-- -->

``` r
smart_survey %>%
  filter(PC_OS=="Windows") %>%
  ggplot(aes(x=num_PC_OS)) +
  geom_bar() +
  ggtitle("Level of satisfaction of Windows users") +
  ylab("") +
  xlab("") +
  expand_limits(x=1)
```

![](eda_viz_files/figure-gfm/unnamed-chunk-10-1.png)<!-- -->

``` r
smart_survey %>%
  ggplot(aes(x=future_PC_OS)) +
  geom_bar() +
  xlab("") +
  ylab("") +
  ggtitle("Future PC Operating System")
```

![](eda_viz_files/figure-gfm/unnamed-chunk-11-1.png)<!-- -->

``` r
smart_survey %>%
  filter(PC_OS %in% c("Windows","MacOS")) %>%
  ggplot(aes(x=PC_OS,y=smartphone_OS)) +
  geom_bin2d() +
  ylab("Smartphone OS") +
  xlab("Laptop OS")
```

![](eda_viz_files/figure-gfm/unnamed-chunk-12-1.png)<!-- -->
